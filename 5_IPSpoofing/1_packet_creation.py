from scapy.all import *

target_ip = "192.168.145.18"
source_ip = "10.0.0.1"

packet = IP()/TCP()
packet.src = source_ip
packet.dst = target_ip
packet.sport = 22
packet.ttl = 33


packet.show()
