#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

data = 'set system host-name R1'

with Device(host='192.168.0.100')  as dev:
    with Config(dev, mode='exclusive') as cu:
        #cu.load(url='/var/tmp/config.conf', overwrite=True)
        cu.load(data, format='set')
        diff = cu.diff()
        if diff is None:
            print("Configuration already up to date")
        else:
            print(diff)
            cu.commit(confirm=1)
