import json
import sys
from json import JSONDecodeError

from .CONFIGS import CONFIG_PROJECT
import time
from .Logger import logger


@logger('functional.log')
def get_presence_message(account_name):
    message = {
        CONFIG_PROJECT['DEFAULT_CONF'].get('ACTION'): CONFIG_PROJECT['DEFAULT_CONF'].get('PRESENCE'),
        CONFIG_PROJECT['DEFAULT_CONF'].get('TIME'): round(time.time(), 2),
        CONFIG_PROJECT['DEFAULT_CONF'].get('USER'): {
            CONFIG_PROJECT['DEFAULT_CONF'].get('ACCOUNT_NAME'): account_name
        }
    }
    return message


@logger('functional.log')
def send(socket, client_message):
    json_obj = json.dumps(client_message)
    response = json_obj.encode(CONFIG_PROJECT['DEFAULT_CONF'].get('ENCODING'))
    socket.send(response)


@logger('functional.log')
def get_message_from_server(socket):
    response = socket.recv(CONFIG_PROJECT['DEFAULT_CONF'].get('MAX_PACKAGE_LENGTH'))
    try:
        response_decode = response.decode(CONFIG_PROJECT['DEFAULT_CONF'].get('ENCODING'))
    except:
        raise JSONDecodeError('Ошибка декодирования')
    return json.loads(response_decode)


@logger('functional.log')
def check_message_on_server(message):
    if CONFIG_PROJECT['DEFAULT_CONF'].get('ACTION') in message \
            and message.get(CONFIG_PROJECT['DEFAULT_CONF'].get('ACTION')) == CONFIG_PROJECT[
        'DEFAULT_CONF'].get('PRESENCE') \
            and CONFIG_PROJECT['DEFAULT_CONF'].get('TIME') in message \
            and CONFIG_PROJECT['DEFAULT_CONF'].get('USER') in message:
        return {CONFIG_PROJECT['DEFAULT_CONF'].get('RESPONSE'): CONFIG_PROJECT['STATUS'].get('OK')}
    return {CONFIG_PROJECT['DEFAULT_CONF'].get('RESPONSE'): CONFIG_PROJECT['STATUS'].get('BAD_REQUEST')}


@logger('functional.log')
def check_message_on_client(message):
    if CONFIG_PROJECT['DEFAULT_CONF'].get('RESPONSE') in message:
        if message.get(CONFIG_PROJECT['DEFAULT_CONF'].get('RESPONSE')) == 200:
            return {
                'status': 'Connected',
                '200': 'OK'
            }

    return {
        'status': 'Canceled',
        '400': f'{CONFIG_PROJECT["DEFAULT_CONF"].get("ERROR")}'
    }


@logger('functional.log')
def create_ip_port(type=None):
    try:
        ip = sys.argv[1]
        port = int(sys.argv[2])
    except Exception:
        print('Некорректные параметры сервера!\nИспользуются стандартные настройки')
        ip = CONFIG_PROJECT['DEFAULT_CONF'].get('DEFAULT_IP_ADDRESS')
        port = CONFIG_PROJECT['DEFAULT_CONF'].get('DEFAULT_PORT')
        return ip,port


    if type == 'client':
        try:
            ip = sys.argv[1]
            port = int(sys.argv[2])
        except Exception:
            print('Некорректные параметры сервера!\nИспользуются стандартные настройки')
            ip = CONFIG_PROJECT['DEFAULT_CONF'].get('DEFAULT_IP_ADDRESS')
            port = CONFIG_PROJECT['DEFAULT_CONF'].get('DEFAULT_PORT')
        return ip, port


@logger('functional.log')
def request_server(read_clients_list, write_clients_list, client_list):
    for read_client_sock in read_clients_list:
        try:
            message = read_client_sock.recv(1024)
            for write_client_sock in write_clients_list:
                try:
                    write_client_sock.send(message)
                except:
                    client_list.remove(write_client_sock)
        except:
            read_clients_list.remove(read_client_sock)
            continue


def create_user_msg(message,username):
    message = {
        CONFIG_PROJECT['DEFAULT_CONF'].get('ACTION'): CONFIG_PROJECT['DEFAULT_CONF'].get('MESSAGE'),
        CONFIG_PROJECT['DEFAULT_CONF'].get('TIME'): round(time.time(), 2),
        CONFIG_PROJECT['DEFAULT_CONF'].get('TO'): "#room_name",
        CONFIG_PROJECT['DEFAULT_CONF'].get('FROM'): username,
        CONFIG_PROJECT['DEFAULT_CONF'].get('MESSAGE'): message
    }
    return message


@logger('functional.log')
def sender_msg(transport,account_name):
    while True:
        message = input()
        msg = create_user_msg(message, account_name)
        send(transport, msg)


@logger('functional.log')
def writer_msg(transport):
    while True:
        message = get_message_from_server(transport)
        print(f'{message["from"]}:{message["msg"]}')


if __name__ == "__main__":
    pass
