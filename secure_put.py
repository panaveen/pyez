#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP

dev = Device(host='192.168.0.101', user='root', passwd='juniper123')

with SCP(dev, progress=True) as scp:
    scp.put("/home/naveen/.ssh/id_rsa.pub", "/var/tmp/")
