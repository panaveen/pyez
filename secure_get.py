#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP

dev = Device('192.168.0.100')
with SCP(dev, progress=True) as scp:
    scp.get('/var/log/messages', local_path='/var/tmp')

