import ipaddress
from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup

def get_mac_vendor(mac):   
    try:
         vendor = MacLookup().lookup(mac)  
    except:
        vendor = "Unknown"
    if vendor == "PCS Systemtechnik GmbH" or vendor == "Oracle Corp":
        vendor = "Virtual Box"
    
    return vendor

def detect_live_hosts(local_ip):
    print("yourIP:",local_ip)
    network = ipaddress.IPv4Network(f"{local_ip}/24", strict=False)
    print(f"Network Range: {network}")
    target_ip = f"{network.network_address}/24"
    ethernet = Ether(dst="ff:ff:ff:ff:ff:ff") # send to all devices 
    arp = ARP(pdst=target_ip)
    packet = ethernet/arp
    # print ("here done ")
    result = srp(packet, timeout=10, verbose=False)[0]  # if cannot getting reply try to increse timeout=7
    live_hosts = []

    for sent, received in result:
        # print(f"Received ARP reply from IP: {received.psrc}, MAC: {received.hwsrc}") 
        host_info = {
            "ip": received.psrc,
            "mac": received.hwsrc,
            "vendor": get_mac_vendor(received.hwsrc)
        }
        live_hosts.append(host_info)
    if live_hosts:
        print("Live Hosts:")
        for host in live_hosts:
            print(f"IP: {host['ip']} | MAC: {host['mac']} | Vendor: {host['vendor']}")
    else:
        print("No live hosts found.")


