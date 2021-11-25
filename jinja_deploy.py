#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import yaml


junos_hosts = ['192.168.0.100', '192.168.0.101']

for host in junos_hosts:
    filename = host + '.yml'
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
        with Device(host) as dev:
            with Config(dev, mode="exclusive") as conf:
                conf.load(template_path="example.j2",
                template_vars=data, format="text")
                conf.pdiff()
                conf.commit()
                print("Configuration loaded successfully")
