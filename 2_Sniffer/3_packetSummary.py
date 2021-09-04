# import Scapy Library

from scapy.all import *

def callback(packet):
#     print("=====================================================")
#     print(packet.show())
    print(f"{packet[IP].src} ==> {packet[IP].dst}")
    print(f"{packet[TCP].sport} ==> {packet[TCP].dport}")
#     print("=====================================================")

data = sniff(filter="tcp and port 80", prn=callback)
