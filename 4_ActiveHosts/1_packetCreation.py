from scapy.all import *

# packet = IP(dst="1.2.3.4")/TCP(sport=22)

packet = IP()/TCP()
packet.dst="1.2.3.4"
packet.sport=22
packet.ttl=33


packet.show()