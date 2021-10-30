from socket import socket, AF_INET, SOCK_STREAM

from function import create_ip_port
from Logger import logger


@logger('listener.log')
def start():
    # Получаем ip,port
    ip, port = create_ip_port(type='client')
    # Открываем сокет
    new_socket = socket(AF_INET, SOCK_STREAM)
    new_socket.connect((ip, port))

    # Получаем ответ от сервера
    while True:
        response = new_socket.recv(1024)
        if response:
            data = response.decode('utf-8')
            print(f'Сообщение от {new_socket}\n{data}')
        else:
            continue


if __name__ == "__main__":
    start()
