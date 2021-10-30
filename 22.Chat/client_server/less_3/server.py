from socket import socket, AF_INET, SOCK_STREAM
import time
from sys import argv
import json
from status import status

ip,port = argv[1:]

s = socket(AF_INET,SOCK_STREAM)
s.bind((ip,int(port)))
s.listen(10)

response = {
    "response":None,
}

while True:
    client,add = s.accept()
    request = client.recv(256)
    data_from_client = json.loads(request)
    print(data_from_client)

    if data_from_client['action'] == "presence":
        response['response'] = status.get('OK')
        response['alert'] = 'Connect'
    else:
        response['response'] = status.get('BAD_REQUEST')
        response['error'] = 'Something wrong'

    response_from_server = json.dumps(response)
    client.send(response_from_server.encode('utf-8'))
    client.close()
