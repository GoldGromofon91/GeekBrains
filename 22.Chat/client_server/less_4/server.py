import sys
import json
import CONFIGS
from socket import socket, AF_INET, SOCK_STREAM
from function import get_from_server, check_message_on_server, send, create_ip_port


def start_server():
    # try:
    #     listen_ip = sys.argv[1]
    #     listen_port = int(sys.argv[2])
    # except Exception:
    #     print('Некорректные параметры сервера!\nИспользуются стандартные настройки')
    #     sys.exit(1)

    ip, port = create_ip_port()
    listen_socket = socket(AF_INET, SOCK_STREAM)
    listen_socket.bind((ip, port))
    listen_socket.listen(CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('MAX_CONNECTIONS'))

    while True:
        client, client_address = listen_socket.accept()
        message = get_from_server(client)
        response = check_message_on_server(message)
        send(client, response)
        client.close()


if __name__ == "__main__":
    start_server()
