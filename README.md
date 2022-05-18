# configure_loopback_addresses_into_multiple_devices
How to configure loopback interfaces in multiples devices. 

This repo is to explain how to configure 100 loopback interfaces in multiple Nokia boxes. It can also be implemented in other vendors. 

Netmiko is used to connect to devices. 

While connecting to each device, the same IP is used. The port for each device is different. 

Netmiko is a multi-vendor SSH Python library that simplifies the process of connecting to network devices via SSH. This library adds vendor-specific logic to paramiko, which is the de-facto SSH library in Python.

A loopback interface is a virtual interface that is always up and reachable as long as at least one of the IP interfaces on the switch is operational. As a result, a loopback interface is useful for debugging tasks since its IP address can always be pinged if any other switch interface is up.

The sample output from one of the node after the code runs: 

![image](https://user-images.githubusercontent.com/94804863/161009053-64972fe2-048d-44da-8778-592cdbd9d3c4.png)
