#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

host = input("Enter device ip:")

with Device(host) as dev:
    sw = SW(dev)
    print(sw.reboot())

