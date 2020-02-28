# google: https://www.google.com/search?ei=6G5ZXv2SDr2N1fAPvem1kAY&q=python+check++port++server+open
# --> https://stackoverflow.com/questions/19196105/how-to-check-if-a-network-port-is-open-on-linux
import socket

host = 'appel.com'
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)
result = sock.connect_ex((host, port))
print(result)
if result == 0:
    state = 'open'
elif result == socket.errno.EAGAIN:
    state = 'timeout'
else:
    state = 'closed'
print('port {prt} at {hst} is {st}'.format(prt=port, hst=host, st=state))


