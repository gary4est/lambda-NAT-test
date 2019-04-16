import json
import socket
from botocore.vendored import requests

host = "test.rebex.net"
port = 22

def lambda_handler(event, context):
    response = requests.get('https://ifconfig.me/')
    nat_ip = response.text
    print ("INFO: external IP:", nat_ip)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((host,port))
    if result == 0:
        print ("INFO: okay, able to connect to {} on port {} via {}".format(host, port, nat_ip))
    else:
        print ("ERROR: unable to connect to {} on port {} via {}".format(host, port, nat_ip))
    return {
        'Port Connection Result': result
    }


