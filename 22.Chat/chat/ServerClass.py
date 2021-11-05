from meta import ServerVerifierMeta, CheckPort, CheckIP


class Server(metaclass=ServerVerifierMeta):
    port = CheckPort()
    ip = CheckIP()



