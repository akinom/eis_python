import socket

for hostname in ['princeton.edu', 'oit.princeton.edu', 'appel.com', 'yahoo.com']:
    ip_adr = socket.gethostbyname(hostname)
    print(ip_adr)
print("-------------------------------------------------------------\n")

for hostname in ['princeton.edu', 'oit.princeton.edu', 'appel.com', 'yahoo.com']:
    ip_adr = socket.gethostbyname(hostname)
    print("{ip} {host}".format(host=hostname, ip=ip_adr))
print("-------------------------------------------------------------\n")

print("\t".join(["ip", "hostname"]))
for hostname in ['princeton.edu', 'oit.princeton.edu', 'appel.com', 'yahoo.com']:
    ip_adr = socket.gethostbyname(hostname)
    print("\t".join([ip_adr, hostname]))
print("-------------------------------------------------------------\n")

