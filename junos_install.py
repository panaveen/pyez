#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

pkg = 'jinstall.tgz'


with Device('192.168.0.100') as dev:
    sw = SW(dev)
    ok, msg = sw.install(package=pkg, validate=True, checksum_algorithm='sha256')
    print("Status:" + str(ok) + ", Message: " + msg)
    if ok:
        sw.reboot()




