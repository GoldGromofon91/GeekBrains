from socket import socket, AF_INET, SOCK_STREAM
import time
from sys import argv
import json

time = time.time()
ip,port = argv[1:]
message_to_server = {
    "action":"presence",
    "time":time,
}

s = socket(AF_INET,SOCK_STREAM)
s.connect((ip,int(port)))
request = json.dumps(message_to_server)
s.send(request.encode('utf-8'))

response = s.recv(256)
data = json.loads(response)
print(data)
