# threat_detection.py
from scapy.all import sniff


def packet_callback(packet):
    print(packet.show())


def start_network_monitor():
    # sniff(prn=packet_callback, filter="ip", store=0)
    sniff(count=10, prn=packet_callback, filter="ip")
