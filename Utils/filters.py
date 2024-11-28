from scapy.all import IP , ICMP , TCP , UDP


def packet_filter(packet, filter_criteria):
    if 'src_ip' in filter_criteria:
        if packet.haslayer(IP) and packet[IP].src != filter_criteria['src_ip']:
            return False

    if 'dst_ip' in filter_criteria:
        if packet.haslayer(IP) and packet[IP].dst != filter_criteria['dst_ip']:
            return False

    if 'protocol' in filter_criteria:
        if packet.haslayer(IP) and packet[IP].proto != filter_criteria['protocol']:
            return False

    if 'src_port' in filter_criteria and packet.haslayer(TCP):
        if packet[TCP].sport != filter_criteria['src_port']:
            return False
    if 'dst_port' in filter_criteria and packet.haslayer(TCP):
        if packet[TCP].dport != filter_criteria['dst_port']:
            return False

    if 'src_udp_port' in filter_criteria and packet.haslayer(UDP):
        if packet[UDP].sport != filter_criteria['src_udp_port']:
            return False
    if 'dst_udp_port' in filter_criteria and packet.haslayer(UDP):
        if packet[UDP].dport != filter_criteria['dst_udp_port']:
            return False

    if 'icmp_type' in filter_criteria and packet.haslayer(ICMP):
        if packet[ICMP].type != filter_criteria['icmp_type']:
            return False

    return True

def parse_filter_string(filter_str):
    filter_dict = {}

    conditions = filter_str.split(' and ')

    for condition in conditions:
        condition = condition.strip().lower()

        if condition.startswith('src host'):
            ip = condition.split(' ')[2]
            filter_dict['src_ip'] = ip
        elif condition.startswith('dst host'):
            ip = condition.split(' ')[2]
            filter_dict['dst_ip'] = ip
        elif 'tcp' in condition:
            filter_dict['protocol'] = 'TCP'
        elif 'udp' in condition:
            filter_dict['protocol'] = 'UDP'
        elif 'icmp' in condition:
            filter_dict['protocol'] = 'ICMP'

    return filter_dict
