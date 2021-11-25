#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device('192.168.0.100').open()
config_text = """
set system host-name TEST
"""
with Config(dev, mode='exclusive') as cu:
    cu.load(config_text, format="set", merge=True)
    cu.pdiff()
    cu.rollback(rb_id=0)
dev.close()
