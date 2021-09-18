from scapy.all import *
conf.verb = 0
TIMEOUT = 2

ip_address = input("Enter an IP address to check status: ")

packet = IP()/ICMP()
packet.dst = ip_address

packet.seq = 1

# packet.show()
response = sr1(packet, timeout=TIMEOUT)
if response is not None:
    print(f"{ip_address} host is UP and running.")
    # print("=========================")
    # response.show()
    # print("=========================")
else:
    print(f"{ip_address} is unreachable.")
