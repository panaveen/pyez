#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError

data = '''
set system host-name R2
set system login user admin uid 2000
set system login user admin class super-user
set system login user admin authentication encrypted-password "$6$9HUEgPSp$QsqMlViXhmI1oyQNELIhgJGs8ZK2zzMpIdLt8xVIoVtmwCPzmadBxFzIkCs7Y2KzxAYXBSWtxkwDc62MAcKUj1"
'''


def main():
    try:
        with Device(host='192.168.0.101')  as dev:
            with Config(dev, mode='exclusive') as cu:
                #cu.load(url='/var/tmp/config.conf', overwrite=True)
                cu.load(data, format='set')
                diff = cu.diff()
                if diff is None:
                    print("Configuration already up to date")
                else:
                    print(diff)
                    cu.commit()
    except ConnectError:
        print("Could not connect to device")


if __name__ == '__main__':
    main()
