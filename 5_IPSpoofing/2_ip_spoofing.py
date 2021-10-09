from scapy.all import *

target_ip = "192.168.145.18"
source_ip = "10.0.0.1"
source_port = 22
dst_port = 80


def createPacket(sport):
    packet = IP()/TCP()
    packet.src = source_ip
    packet.dst = target_ip
    packet.sport = sport
    packet.dport = dst_port
    packet.show()
    return packet


if __name__ == "__main__":
    for i in range(10):
        packet = createPacket(i)
        send(packet, iface="usb0")
