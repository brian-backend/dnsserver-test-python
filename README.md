# dnsserver-test-python

This project is for simulating DNS attacks.

## Prerequests

In order to use those codes, some python packages should be installed.

`pip install dnslib scapy`


## Too Many Requests

We try to request DNS resolve with already registered domains/records.

We can set rate per second by changing:

`flood_rate = 500 # Queries per second`

Acoording to this request, we can test if rate limitation of dns server is working properly.


## DNS NXDOMAIN Attack

With this code, we can attack dns server by requesting non-existing domains/records.

We can set domain/record pattern with `random_name()` function

`def random_name():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3)) + 'domain.com' # change domain.com into already registered domain name.
`

If we need to test non-exsiting subdomain attack, we can set `domain.com` as already registered domain name.

## DNS Amplification Attack

With this code, we can attack dns server with different IPs.

