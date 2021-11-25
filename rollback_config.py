#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

with Device(host='192.168.0.100') as dev:
    with Config(dev, mode='exclusive') as cu:
        print("Rolling back")
        cu.rollback(rb_id=1)
        cu.commit()
        print("Device configuration rolled back")
