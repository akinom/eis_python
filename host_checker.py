import socket

def v0():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 80))
    if result == 0:
        print("Port is open")
    else:
        print("Port is not open")
    sock.close()


def port_is_open(host, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def get_ipaddr(hostname):
    return socket.gethostbyname(hostname)

def print_tsv_header(props):
    for p in props:
        print(p, end='\t')
    print()

def print_tsv(dict, props):
    for p in props:
        print(dict[p], end='\t')
    print()

def readlines_stripped(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    stripped_lines = []
    for l in lines:
        stripped_lines.append(l.strip())
    return stripped_lines

def vfinally(hostfile, ports):
    hostlist = readlines_stripped(hostfile)
    headers = ['ip'] + ports  + ['name']
    print_tsv_header(headers)
    for server in hostlist:
        server_props = {}
        server_props['name'] = server
        server_props['ip'] = get_ipaddr(server)
        for port in ports:
            server_props[port] =  port_is_open(server, port, 1)
        print_tsv(server_props, headers )


print("#Running on {}".format(socket.gethostname()))
vfinally('eis/hosts.txt', [80, 443, 22])