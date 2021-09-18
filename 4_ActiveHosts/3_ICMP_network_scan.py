from scapy.all import *
import ipaddress

conf.verb = 0
TIMEOUT = 0.3

ip_address_CIDR = input("Enter an IP address range [CIDR]: ")

ip_range_list = [str(ip) for ip in ipaddress.IPv4Network(ip_address_CIDR)]
# print(ip_range_list)

packet = IP()/ICMP()

for index, ip in enumerate(ip_range_list):
    packet.dst = ip
    packet.seq = index

    # packet.show()
    response = sr1(packet, timeout=TIMEOUT)
    if response is not None:
        print(f"{ip} host is UP and running.")
    else:
        print(f"{ip} is unreachable.")
