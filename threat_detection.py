from scapy.all import sniff

times_found_dict = {}

PROTOCOL_LOOKUP = {
    1: "ICMP",
    2: "IGMP",
    6: "TCP",
    17: "UDP",
    41: "IPv6",
    89: "OSPF",
    132: "SCTP",
}


def increment_or_add_to_dict(protocol):
    if protocol in times_found_dict.keys():
        times_found_dict[protocol] += 1
    else:
        times_found_dict[protocol] = 1


def packet_callback(packet):
    if packet.haslayer("IP"):
        protocol_num = packet["IP"].proto
        packet_protocol = PROTOCOL_LOOKUP.get(protocol_num, str(protocol_num))
        increment_or_add_to_dict(packet_protocol)
        # this print shows the full content of the packet, leave it be
        # print(packet.show())


def start_network_monitor():
    capture = sniff(count=10, prn=packet_callback, filter="ip")
    capture.summary()
    print(times_found_dict)
