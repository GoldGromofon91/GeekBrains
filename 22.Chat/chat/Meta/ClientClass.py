from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

from .Logger import logger
from .function import get_presence_message, send, get_message_from_server, check_message_on_client, sender_msg, \
    writer_msg
from .meta import CheckPort, CheckIP, CheckName


class GeneralClient():
    port = CheckPort()
    ip = CheckIP()
    name = CheckName()

    def __init__(self):
        self.client_socket = None
    @logger('functional.log')
    def run(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((self.ip, self.port))
        user_name = input('Enter username: ')
        self.name = user_name
        message = get_presence_message(user_name)
        send(client_socket, message)

        # Получаем ответ от сервера
        response = get_message_from_server(client_socket)
        output = check_message_on_client(response)

        if output:
            print('You are in chat')
        else:
            raise Exception('Error connect')

        sender = Thread(target=sender_msg, kwargs={'transport': client_socket, 'account_name': user_name})
        sender.start()

        writer = Thread(target=writer_msg, kwargs={'transport': client_socket})
        writer.start()


class ClientConf_1(GeneralClient):
    pass
