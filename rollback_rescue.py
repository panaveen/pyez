#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


with Device(host='192.168.0.100') as dev:
    with Config(dev, mode='exclusive') as cu:
        rescue = cu.rescue(action='reload')
        if rescue is False:
            print("No rescue configuration")
        else:
            cu.commit()
            print("rescue configuratio successfully")
