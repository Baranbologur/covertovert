import scapy


from scapy.all import sniff, IP, ICMP

def ttl_filter(frame):
    if frame.haslayer(ICMP) and frame[IP].ttl == 1:
        return True
    return False

if __name__ == "__main__":
    packets = sniff(count=1, lfilter=ttl_filter)
    if packets:
        packets[0].show()
# Implement your ICMP receiver here
