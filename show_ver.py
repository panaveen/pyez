#!/usr/bin/python3

from jnpr.junos import Device
from lxml import etree
from pprint import pprint

with Device('192.168.0.100') as dev:
    sw = dev.rpc.get_software_information({'format':'text'})
    pprint(etree.tostring(sw, encoding='unicode'))
