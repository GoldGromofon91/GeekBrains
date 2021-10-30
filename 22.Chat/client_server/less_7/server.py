import select

import CONFIGS
from socket import socket, AF_INET, SOCK_STREAM
from function import create_ip_port, request_server



def start_server():
    ip, port = create_ip_port()

    listen_socket = socket(AF_INET, SOCK_STREAM)
    listen_socket.bind((ip, port))
    listen_socket.listen(CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('MAX_CONNECTIONS'))
    listen_socket.settimeout(0.3)

    client_list = []

    while True:
        try:
            client, addr = listen_socket.accept()
            client_list.append(client)
        except OSError:
            pass


        try:
            read_clients, write_clients, error = select.select(client_list, client_list, [], 0)
        except:
            pass

        request_server(read_clients,write_clients,client_list)


if __name__ == "__main__":
    start_server()
