import dis
import re
import socket


class ClientVerifierMeta(type):

    def __init__(self, clsname, bases, clsdict):
        self.verify_socket(clsname, clsdict)
        type.__init__(self, clsname, bases, clsdict)

    @staticmethod
    def verify_socket(clsname, clsdict):
        """
        Проверяет Client socket на:
        - отсутствие создания сокетов на уровне классов
        - отсутствие вызовов методов сервера (listen, accept)
        - использование TCP соединения в сокетах
        """

        socket_store = None
        for key, value in clsdict.items():
            assert not isinstance(value, socket.socket), 'Creating sockets at the class level is forbidden'

            instructions = dis.get_instructions(value)
            for inst in instructions:
                if inst.argval == 'socket' and inst.opname == 'LOAD_GLOBAL':
                    while inst.opname != 'STORE_ATTR':
                        inst = next(instructions)
                        if inst.opname == 'LOAD_ATTR' and inst.arg == 2:
                            assert inst.argval == 'SOCK_STREAM', 'Only TCP connection is available!'
                    socket_store = inst.argval

        if socket_store:
            for key, value in clsdict.items():
                forbidden_methods = ['listen', 'accept']
                instructions = dis.get_instructions(value)
                for inst in instructions:
                    if inst.argval == socket_store:
                        next_inst = next(instructions)
                        # LOAD_METHOD -> LOAD_ATTR
                        assert not (next_inst.argval in forbidden_methods and next_inst.opname == 'LOAD_ATTR'), \
                            f"{clsname} socket should not call method '{next_inst.argval}'"


class ServerVerifierMeta(type):

    def __init__(self, clsname, bases, clsdict):
        self.verify_socket(clsname, clsdict)
        type.__init__(self, clsname, bases, clsdict)

    @staticmethod
    def verify_socket(clsname, clsdict):
        socket_store = None
        for key, value in clsdict.items():
            assert not isinstance(value, socket.socket), 'Creating sockets at the class level is forbidden'

            try:
                instructions = dis.get_instructions(value)
            except TypeError:
                continue

            for inst in instructions:
                if inst.argval == 'socket' and inst.opname == 'LOAD_GLOBAL':
                    while inst.opname != 'STORE_ATTR':
                        inst = next(instructions)
                        if inst.opname == 'LOAD_ATTR' and inst.arg == 2:
                            assert inst.argval == 'SOCK_STREAM', 'Only TCP connection is available!'
                    socket_store = inst.argval

        if socket_store:
            forbidden_methods = ['connect']
            for key, value in clsdict.items():
                try:
                    instructions = dis.get_instructions(value)
                except TypeError:
                    continue

                for inst in instructions:
                    if inst.argval == socket_store:
                        next_inst = next(instructions)
                        # LOAD_METHOD -> LOAD_ATTR
                        assert not (next_inst.argval in forbidden_methods and next_inst.opname == 'LOAD_ATTR'), \
                            f"{clsname} socket should not call method '{next_inst.argval}'"


class CheckPort:
    def __init__(self):
        self._port = 7777

    def __get__(self, instance, owner=None):
        return self._port

    def __set__(self, instance, value):
        if not (isinstance(value, int) or value >= 0):
            raise ValueError("некорректное значение")
        self._port = value


class CheckIP:
    def __init__(self):
        self._ip = '127.0.0.1'

    def __get__(self, instance, owner=None):
        return self._ip

    def __set__(self, instance, value):
        if not isinstance(value, str) or value:
            raise ValueError("некорректное значение")
        match = re.search(r'^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$', value)
        if match:
            setattr(instance, self._ip, value)


class CheckName:
    def __init__(self, name='User'):
        self._name = name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        value = str(value)
        setattr(instance, self._name, value)
