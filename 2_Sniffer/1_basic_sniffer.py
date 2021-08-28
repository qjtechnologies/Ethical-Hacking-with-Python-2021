# import Scapy Library

from scapy.all import *

data = sniff(filter="icmp", count=10)

for packet in data:
    print("=====================================================")
    print(packet.show())
    print("=====================================================")

print(data)