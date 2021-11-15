import select
from socket import socket, AF_INET, SOCK_STREAM

from .CONFIGS import CONFIG_PROJECT
from .Logger import logger
from .meta import ServerVerifierMeta, CheckIP, CheckPort
from .function import get_message_from_server, send, check_message_on_server
from .db_conf import ServerDB
from .models import Base


class GeneralServer(metaclass=ServerVerifierMeta):
    port = CheckPort()
    ip = CheckIP()

    def __init__(self):
        self.lsocket = None
        self.db = None
        self.client_list = []
        self.read_clients = []
        self.write_clients = []
        self.error = []
        self.user_messages = []

    @logger('functional.log')
    def create_connection(self):
        self.lsocket = socket(AF_INET, SOCK_STREAM)
        self.lsocket.bind((self.ip, self.port))
        self.lsocket.listen(CONFIG_PROJECT['DEFAULT_CONF'].get('MAX_CONNECTIONS'))
        self.lsocket.settimeout(0.3)

    @logger('functional.log')
    def accept_connection(self):
        try:
            client, addr = self.lsocket.accept()
        except OSError:
            pass
        else:
            self.client_list.append(client)

    @logger('functional.log')
    def init_db(self):
        self.db = ServerDB(base=Base,db_name='server.sqlite')
        self.db.open_connect()

    @logger('functional.log')
    def run(self):
        self.create_connection()
        self.init_db()

        while True:
            self.accept_connection()
            try:
                self.read_clients, self.write_clients, self.error = select.select(self.client_list, self.client_list,[], 0)
            except:
                pass

            if self.read_clients:
                for read_user_socket in self.read_clients:
                    message = get_message_from_server(read_user_socket)

                    if message['action'] == 'presence':
                        response = check_message_on_server(message)
                        try:
                            send(read_user_socket, response)
                        except:
                            self.read_clients.remove(read_user_socket)
                            pass

                    if message['action'] == 'msg':
                        self.user_messages.append(message)

            if self.user_messages and self.write_clients:
                for message in self.user_messages:
                    for waiting_user in self.write_clients:
                        send(waiting_user, message)
                    self.user_messages.remove(message)


class ServerConf_1(GeneralServer):
    pass
