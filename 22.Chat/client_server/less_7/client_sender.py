from socket import socket, AF_INET, SOCK_STREAM

from function import create_ip_port


def start():
    # Получаем ip,port
    ip, port = create_ip_port(type='client')
    # Открываем сокет
    new_socket = socket(AF_INET, SOCK_STREAM)
    new_socket.connect((ip, port))

    while True:
        message = input('Enter message: ').encode('utf-8')
        new_socket.send(message)


if __name__ == "__main__":
    start()
