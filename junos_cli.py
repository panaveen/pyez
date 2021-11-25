#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell


with  Device(host='192.168.0.100') as dev:
    print(dev.facts)
