#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError, CommitError

data = '''
set system domain-name test.com
'''

device_list = ['192.168.0.100', '192.168.0.101']

def conf(device):
    with Device(host=device)  as dev:
        with Config(dev, mode='exclusive') as cu:
            #cu.load(url='/var/tmp/config.conf', overwrite=True)
            cu.load(data, format='set')
            diff = cu.diff()
            if diff is None:
                print("Configuration already up to date")
            else:
                print(diff)
                user_confim = input("Commit?")
                if user_confim == "Y":
                    cu.commit()
                else:
                    print("Rolling back")    
                    cu.rollback(rb_id=0)


def main():
    try:
        for device in device_list:
            print("Connecting to {}".format(device))
            conf(device)
    except ConnectError:
        print("Could not connect to device")
    except CommitError:
        print("Device configuration did not commit successfully")


if __name__ == '__main__':
    main()
