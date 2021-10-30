import CONFIGS
from socket import socket, AF_INET, SOCK_STREAM
from function import get_from_server, check_message_on_server, send, create_ip_port
from Logger import logger



def start_server():

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
