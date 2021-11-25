#!/usr/bin/python3

from jnpr.junos import Device

#dev = Device('192.168.0.100')
with Device('192.168.0.100') as dev:
    route_lxml_element =dev.rpc.get_route_information(table='inet.0')
    list_of_routes = route_lxml_element.findall('.//rt')
    for route in list_of_routes:
        print(route)
