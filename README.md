# Network_Host_Discovery_Via_ICMP_Ping
Working Principle :
This Python program, using Scapy, performs network host discovery by sending ICMP Echo Requests (ping) to every possible host within a specified subnet (CIDR range). The working principle follows these steps:

* User Input : The user provides a network in CIDR notation (e.g., 192.168.1.0/24).

* IP Range Extraction : The program converts the CIDR notation into a list of IP addresses (excluding network and broadcast addresses).

* ICMP Ping Requests : Each IP address is sent an ICMP Echo Request (ping).

* Response Handling : If an ICMP Echo Reply is received, the IP address is considered active and stored in a list.

* Output Results : The program displays the list of active hosts in the network.

This script is useful for network scanning, troubleshooting connectivity, and identifying live devices on a subnet.
