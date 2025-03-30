from scapy.all import *
import ipaddress

def ping_hosts_in_network(network_cidr, timeout=1):
    # Convert the network into an ipaddress network object
    try:
        network = ipaddress.ip_network(network_cidr)
    except ValueError:
        print("Invalid network address. Please enter a valid CIDR notation, e.g., '192.168.1.0/24'")
        return

    # Prepare a list to store active hosts
    active_hosts = []

    print(f"Pinging hosts in network: {network_cidr}")

    # Loop through all IP addresses in the network
    for ip in network.hosts():
        # Send an ICMP echo request (ping) to each host
        packet = IP(dst=str(ip))/ICMP()
        reply = sr1(packet, timeout=timeout, verbose=0)

        # If a reply is received, the host is active
        if reply:
            active_hosts.append(str(ip))
            print(f"Host {ip} is active")

    # Print the list of active hosts
    if active_hosts:
        print("\nActive hosts in the network:")
        for host in active_hosts:
            print(host)
    else:
        print("No active hosts found in the network.")

# Get network address from user and run the function
if __name__ == "__main__":
    network_cidr = input("Enter the network address in CIDR notation (e.g., '192.168.1.0/24'): ")
    ping_hosts_in_network(network_cidr)
