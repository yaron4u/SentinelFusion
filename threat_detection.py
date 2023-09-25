from scapy.all import sniff

times_found_dict = {}


def increment_or_add_to_dict(protocol):
    if protocol in times_found_dict.keys():
        times_found_dict[protocol] += 1
    else:
        times_found_dict[protocol] = 1


def packet_callback(packet):
    if packet.haslayer("IP"):
        packet_protocol = packet["IP"].proto
        increment_or_add_to_dict(packet_protocol)
        # this print shows the full content of the packet, leave it be
        # print(packet.show())


def start_network_monitor():
    capture = sniff(count=10, prn=packet_callback, filter="ip")
    capture.summary()
    print(times_found_dict)
