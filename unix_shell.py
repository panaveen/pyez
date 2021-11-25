#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell
from pprint import pprint


dev = Device('192.168.0.100')
ss = StartShell(dev)
ss.open()
software = ss.run("ls -la /var/tmp")
pprint(software)
ss.close()
