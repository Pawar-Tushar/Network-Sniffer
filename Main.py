import argparse
import hashlib
import os
import sys
from getpass import getpass
from Utils.capture import start_capture
from Utils.filters import parse_filter_string
from Utils.analysis import analyze_packet
from Utils.save import save_to_txt, save_to_pcap
from Utils.HostDetector import detect_live_hosts

PASSWORD_FILE = "password_hash.txt"  # dont touch this file dont do any changes there  if you are facing problem simply delete it and Run App Again
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(input_password):
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as f:
            stored_hash = f.read().strip()
            return stored_hash == hash_password(input_password)
    return False

def set_password():
    password = getpass("Set a new password: ")
    confirm_password = getpass("Confirm password: ")
    
    if password != confirm_password:
        print("Passwords do not match.")
        sys.exit(1)
    
    with open(PASSWORD_FILE, 'w') as f:
        f.write(hash_password(password))
    print("Password set successfully.")

def login():
    if not os.path.exists(PASSWORD_FILE):
        print("No password set. Please set a new password.")
        set_password()
    
    while True:
        password = getpass("Enter password: ")
        if verify_password(password):
            print("Login successful.")
            break
        else:
            print("Incorrect password. Please try again.")

def start_application(args):
    if args.option == "c":
        filter_criteria = parse_filter_string(args.f)
        captured_packets = start_capture(args.i, args.pc, filter_criteria)

        if not captured_packets:
            print("No packets captured.")
            return

        if args.a:
            print(f"Analyzing {args.pc} packets...")
            for packet in captured_packets:
                analyze_packet(packet)

        if args.s:
            if args.p:
                save_to_pcap(captured_packets, args.p)
            elif args.t:
                save_to_txt(captured_packets, args.t)
            else:
                print("No save option selected. Please choose to save packets as either file.PCAP or file.TXT type file only.")

    elif args.option == "lh":
        if args.ip:
            detect_live_hosts(args.ip)
        else:
            print("For live host detection, please provide an IP address using --ip")
            sys.exit(1)

    else:
        print("Invalid option. Use 'c' for capture or 'lh' for live host detection.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Network Sniffer Application")

    parser.add_argument("option", choices=["c", "lh"], help="Choose an option: 'c' for capture or 'lh' for live host detection")
    parser.add_argument("--i", help="Network interface to capture on (e.g., eth0, Wi-Fi)", required=False)
    parser.add_argument("--f", help="Filter condition (e.g., 'src host 192.168.1.1 and tcp')", default="all")
    parser.add_argument("--pc", help="Number of packets to capture", type=int, required=False)
    parser.add_argument("--a", help="Analyze captured packets", action="store_true")
    parser.add_argument("--s", help="Save captured packets", action="store_true")
    parser.add_argument("--t", help="Save captured packets in txt format (provide filename)", type=str)
    parser.add_argument("--p", help="Save captured packets in pcap format (provide filename)", type=str)
    parser.add_argument("--ip", help="IP address for live host detection (e.g., 192.168.1.104)", required=False)

    args = parser.parse_args()
    if args.option == "c":
        if not args.i or not args.pc:
            print("For packet capture, both '--i' (interface) and '--pc' (packet count) are required.")
            sys.exit(1)

    login()
    start_application(args)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")


