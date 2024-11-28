#tusharpawar749964@gmail.com
from scapy.all import wrpcap

captured_packets = []

def save_to_txt(captured_packets, filename):
    try:
        with open(filename, 'w') as f:
            for packet in captured_packets:
                f.write(packet.summary() + '\n')
        print(f"Packets saved to {filename}")
    except Exception as e:
        print(f"Error saving packets to TXT: {e}")

def save_to_pcap(captured_packets, filename):
    try:
        wrpcap(filename, captured_packets)
        print(f"Packets saved to {filename}")
    except Exception as e:
        print(f"Error saving packets to PCAP: {e}")
