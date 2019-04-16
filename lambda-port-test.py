import socket
import requests

host = "test.rebex.net"
port = 22

response = requests.get('https://ifconfig.me/')
nat_ip = response.text

print ("INFO: testing connection to {} on port {} via {}".format(host, port, nat_ip))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)
result = sock.connect_ex((host,port))
if result == 0:
    print ("INFO: okay, able to connect to {} on port {} via {}".format(host, port, nat_ip))
else:
    print ("ERROR: unable to connect to {} on port {} via {}".format(host, port, nat_ip))

