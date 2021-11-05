from meta import ClientVerifierMeta, CheckPort, CheckIP, CheckName


class Client():
    port = CheckPort()
    ip = CheckIP()
    name = CheckName()