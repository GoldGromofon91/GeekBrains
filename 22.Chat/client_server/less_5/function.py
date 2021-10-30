import json
import sys
from json import JSONDecodeError

import CONFIGS
import time
from Logger import logger


@logger('functional.log')
def get_template_message(role):
    message = {
        CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('ACTION'): CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('PRESENCE'),
        CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('TIME'): round(time.time(),2),
        CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('USER'): role
    }
    return message

@logger('functional.log')
def send(socket, client_message):
    json_obj = json.dumps(client_message)
    response = json_obj.encode(CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('ENCODING'))
    socket.send(response)

@logger('functional.log')
def get_from_server(socket):
    response = socket.recv(CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('MAX_PACKAGE_LENGTH'))
    try:
        response_decode = response.decode(CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('ENCODING'))
    except:
        raise JSONDecodeError('Ошибка декодирования')
    return json.loads(response_decode)

@logger('functional.log')
def check_message_on_server(message):
    if CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('ACTION') in message \
            and message.get(CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('ACTION')) == CONFIGS.CONFIG_PROJECT[
        'DEFAULT_CONF'].get('PRESENCE') \
            and CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('TIME') in message \
            and CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('USER') in message \
            and message.get(CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('USER')) == 'Guest':
        return {CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('RESPONSE'): CONFIGS.CONFIG_PROJECT['STATUS'].get('OK')}
    return {CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('RESPONSE'): CONFIGS.CONFIG_PROJECT['STATUS'].get('BAD_REQUEST')}

@logger('functional.log')
def check_message_on_client(message):
    if CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('RESPONSE') in message:
        if message.get(CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('RESPONSE')) == 200:
            return {
                'status': 'Connected',
                '200': 'OK'
            }

    return {
        'status': 'Canceled',
        '400': f'{CONFIGS.CONFIG_PROJECT["DEFAULT_CONF"].get("ERROR")}'
    }

@logger('functional.log')
def create_ip_port(type=None):
    try:
        ip = sys.argv[1]
        port = int(sys.argv[2])
    except Exception:
        print('Некорректные параметры сервера!\nИспользуются стандартные настройки')
        sys.exit(1)
    return ip, port

    if type == 'client':
        try:
            ip = sys.argv[1]
            port = int(sys.argv[2])
        except Exception:
            print('Некорректные параметры сервера!\nИспользуются стандартные настройки')
            ip = CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('DEFAULT_IP_ADDRESS')
            port = CONFIGS.CONFIG_PROJECT['DEFAULT_CONF'].get('DEFAULT_PORT')
        return ip,port

if __name__ == "__main__":
    mess = get_template_message('Guest')
