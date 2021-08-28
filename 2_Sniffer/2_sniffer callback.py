# import Scapy Library

from scapy.all import *

def callback(packet):
    print("=====================================================")
    print(packet.show())
    print("=====================================================")

data = sniff(filter="icmp", prn=callback)

# for packet in data:
#     print("=====================================================")
#     print(packet.show())
#     print("=====================================================")

# print(data)