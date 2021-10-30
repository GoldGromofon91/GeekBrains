import json
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
import CONFIGS
from function import get_template_message, send, get_from_server, check_message_on_client, create_ip_port


def start():
    #Получаем ip,port
    ip,port = create_ip_port(type='client')
    # Открываем сокет
    new_socket = socket(AF_INET,SOCK_STREAM)
    new_socket.connect((ip,port))
    message = get_template_message(role='Guest')
    send(new_socket,message)

    # Получаем ответ от сервера
    response = get_from_server(new_socket)
    output = check_message_on_client(response)
    print(output)

if __name__ == "__main__":
    start()
