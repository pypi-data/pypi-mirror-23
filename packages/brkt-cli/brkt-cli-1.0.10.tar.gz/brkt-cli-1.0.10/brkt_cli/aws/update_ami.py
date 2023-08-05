# Copyright 2017 Bracket Computing, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# https://github.com/brkt/brkt-cli/blob/master/LICENSE
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and
# limitations under the License.

"""
Create an encrypted AMI (with new metavisor) based
on an existing encrypted AMI.

Before running brkt updaet-encrypted-ami, set the AWS_ACCESS_KEY_ID and
AWS_SECRET_ACCESS_KEY environment variables, like you would when
running the AWS command line utility.
"""

import json
import logging
import os

from brkt_cli import encryptor_service
from brkt_cli.aws.aws_service import (
    wait_for_instance, stop_and_wait,
    wait_for_image, create_encryptor_security_group, clean_up,
    log_exception_console, wait_for_volume_attached
)
from brkt_cli.encryptor_service import (
    wait_for_encryptor_up,
    wait_for_encryption,
)
from brkt_cli.instance_config import (
    InstanceConfig,
    INSTANCE_UPDATER_MODE,
)
from brkt_cli.user_data import gzip_user_data
from brkt_cli.util import Deadline
from brkt_cli.aws.aws_constants import (
    NAME_GUEST_CREATOR, DESCRIPTION_GUEST_CREATOR, NAME_METAVISOR_UPDATER,
    DESCRIPTION_METAVISOR_UPDATER, NAME_ENCRYPTED_ROOT_SNAPSHOT,
    NAME_METAVISOR_ROOT_SNAPSHOT
)

log = logging.getLogger(__name__)


def update_ami(aws_svc, encrypted_ami, updater_ami, encrypted_ami_name,
               subnet_id=None, security_group_ids=None,
               enc_svc_class=encryptor_service.EncryptorService,
               guest_instance_type='m4.large',
               updater_instance_type='m4.large',
               instance_config=None,
               status_port=encryptor_service.ENCRYPTOR_STATUS_PORT):
    encrypted_guest = None
    updater = None
    mv_root_id = None
    temp_sg_id = None
    if instance_config is None:
        instance_config = InstanceConfig(mode=INSTANCE_UPDATER_MODE)

    try:
        guest_image = aws_svc.get_image(encrypted_ami)

        # Step 1. Launch encrypted guest AMI
        # Use 'updater' mode to avoid chain loading the guest
        # automatically. We just want this AMI/instance up as the
        # base to create a new AMI and preserve license
        # information embedded in the guest AMI
        log.info("Launching encrypted guest/updater")

        instance_config.brkt_config['status_port'] = status_port

        encrypted_guest = aws_svc.run_instance(
            encrypted_ami,
            instance_type=guest_instance_type,
            ebs_optimized=False,
            subnet_id=subnet_id,
            user_data=json.dumps(instance_config.brkt_config))
        aws_svc.create_tags(
            encrypted_guest.id,
            name=NAME_GUEST_CREATOR,
            description=DESCRIPTION_GUEST_CREATOR % {'image_id': encrypted_ami}
        )
        # Run updater in same zone as guest so we can swap volumes

        user_data = instance_config.make_userdata()
        compressed_user_data = gzip_user_data(user_data)

        # If the user didn't specify a security group, create a temporary
        # security group that allows brkt-cli to get status from the updater.
        run_instance = aws_svc.run_instance
        if not security_group_ids:
            vpc_id = None
            if subnet_id:
                subnet = aws_svc.get_subnet(subnet_id)
                vpc_id = subnet.vpc_id
            temp_sg_id = create_encryptor_security_group(
                aws_svc, vpc_id=vpc_id, status_port=status_port).id
            security_group_ids = [temp_sg_id]

            # Wrap with a retry, to handle eventual consistency issues with
            # the newly-created group.
            run_instance = aws_svc.retry(
                aws_svc.run_instance,
                error_code_regexp='InvalidGroup\.NotFound'
            )

        updater = run_instance(
            updater_ami,
            instance_type=updater_instance_type,
            user_data=compressed_user_data,
            ebs_optimized=False,
            subnet_id=subnet_id,
            placement=encrypted_guest.placement,
            security_group_ids=security_group_ids)
        aws_svc.create_tags(
            updater.id,
            name=NAME_METAVISOR_UPDATER,
            description=DESCRIPTION_METAVISOR_UPDATER,
        )
        wait_for_instance(aws_svc, encrypted_guest.id, state="running")
        log.info("Launched guest: %s Updater: %s" %
             (encrypted_guest.id, updater.id)
        )

        # Step 2. Wait for the updater to finish and stop the instances
        aws_svc.stop_instance(encrypted_guest.id)

        updater = wait_for_instance(aws_svc, updater.id, state="running")
        host_ips = []
        if updater.ip_address:
            host_ips.append(updater.ip_address)
        if updater.private_ip_address:
            host_ips.append(updater.private_ip_address)
            log.info('Adding %s to NO_PROXY environment variable' %
                 updater.private_ip_address)
            if os.environ.get('NO_PROXY'):
                os.environ['NO_PROXY'] += "," + \
                    updater.private_ip_address
            else:
                os.environ['NO_PROXY'] = updater.private_ip_address

        enc_svc = enc_svc_class(host_ips, port=status_port)
        log.info('Waiting for updater service on %s (port %s on %s)',
                 updater.id, enc_svc.port, ', '.join(host_ips))
        try:
            wait_for_encryptor_up(enc_svc, Deadline(600))
        except:
            log.error('Unable to connect to encryptor instance.')
            raise

        try:
            wait_for_encryption(enc_svc)
        except Exception as e:
            # Stop the updater instance, to make the console log available.
            stop_and_wait(aws_svc, updater.id)
            log_exception_console(aws_svc, e, updater.id)
            raise

        aws_svc.stop_instance(updater.id)
        encrypted_guest = wait_for_instance(
            aws_svc, encrypted_guest.id, state="stopped")
        updater = wait_for_instance(aws_svc, updater.id, state="stopped")

        guest_bdm = encrypted_guest.block_device_mapping
        updater_bdm = updater.block_device_mapping

        # Step 3. Detach old BSD drive(s) and delete from encrypted guest
        d_list = [encrypted_guest.root_device_name]
        for d in d_list:
            log.info("Detaching old metavisor disk: %s from %s" %
                (guest_bdm[d].volume_id, encrypted_guest.id))
            aws_svc.detach_volume(guest_bdm[d].volume_id,
                    instance_id=encrypted_guest.id,
                    force=True
            )
            aws_svc.delete_volume(guest_bdm[d].volume_id)

        # Step 4. Snapshot MV volume(s)
        log.info("Creating snapshots")
        # Use guest_instance as base instance for create_image
        boot_snap_name = NAME_METAVISOR_ROOT_SNAPSHOT
        root_device_name = guest_image.root_device_name
        guest_root = '/dev/sdf'
        d_list.append(guest_root)

        # Preserve volume type for any additional attached volumes
        for d in guest_bdm.keys():
            if d not in d_list:
                log.debug("Preserving volume type for disk %s", d)
                vol_id = guest_bdm[d].volume_id
                vol = aws_svc.get_volume(vol_id)
                guest_bdm[d].volume_type = vol.type

        # Step 5. Move new MV boot disk to base instance
        log.info("Detach boot volume from %s" % (updater.id,))
        mv_root_id = updater_bdm['/dev/sda1'].volume_id
        aws_svc.detach_volume(mv_root_id,
            instance_id=updater.id,
            force=True
        )

        # Step 6. Attach new boot disk to guest instance
        log.info("Attaching new metavisor boot disk: %s to %s" %
            (mv_root_id, encrypted_guest.id)
        )
        aws_svc.attach_volume(mv_root_id, encrypted_guest.id, root_device_name)
        encrypted_guest = wait_for_volume_attached(
            aws_svc, encrypted_guest.id, root_device_name)
        guest_bdm[root_device_name] = \
            encrypted_guest.block_device_mapping[root_device_name]
        guest_bdm[root_device_name].delete_on_termination = True
        guest_bdm[root_device_name].volume_type = 'gp2'
        guest_root_vol_id = guest_bdm[guest_root].volume_id
        guest_root_vol = aws_svc.get_volume(guest_root_vol_id)
        guest_bdm[guest_root].volume_type = guest_root_vol.type
        if guest_root_vol.type == 'io1':
            guest_bdm[guest_root].iops = guest_root_vol.iops

        # Step 7. Create new AMI. Preserve billing/license info
        log.info("Creating new AMI")
        ami = aws_svc.create_image(
            encrypted_guest.id,
            encrypted_ami_name,
            description=guest_image.description,
            no_reboot=True,
            block_device_mapping=guest_bdm
        )
        wait_for_image(aws_svc, ami)
        image = aws_svc.get_image(ami, retry=True)
        aws_svc.create_tags(
            image.block_device_mapping[root_device_name].snapshot_id,
            name=boot_snap_name,
        )
        aws_svc.create_tags(
            image.block_device_mapping[guest_root].snapshot_id,
            name=NAME_ENCRYPTED_ROOT_SNAPSHOT,
        )
        aws_svc.create_tags(ami)
        return ami
    finally:
        instance_ids = set()
        volume_ids = set()
        sg_ids = set()

        if encrypted_guest:
            instance_ids.add(encrypted_guest.id)
        if updater:
            instance_ids.add(updater.id)
        if mv_root_id:
            volume_ids.add(mv_root_id)
        if temp_sg_id:
            sg_ids.add(temp_sg_id)

        clean_up(aws_svc,
                 instance_ids=instance_ids,
                 volume_ids=volume_ids,
                 security_group_ids=sg_ids)
