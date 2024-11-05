import scapy
from scapy.all import IP, ICMP, send

if __name__ == "__main__":
    packet = IP(dst="receiver", ttl=1) / ICMP()
    send(packet)
# Implement your ICMP sender here
