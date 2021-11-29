import copy


class SSH:
    def __init__(self, user: str, pwd: str, ip: str):
        self.user = user
        self.pwd = pwd
        self.ip = ip
        self.set_defaults()

    def set_defaults(self):
        self.connected = False
        self.call_timeout = 60
        self.port = 22

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def default_ssh(self, port: int = 22):
        ssh_clone = copy.deepcopy(self)
        ssh_clone.set_defaults()
        ssh_clone.port = port
        return ssh_clone

    def port23_ssh(self, port: int = 23):
        ssh_clone = copy.deepcopy(self)
        ssh_clone.set_defaults()
        ssh_clone.port = port
        return ssh_clone





ssh2 = ssh1.port23_ssh()
ssh2.connect()

ssh3 = ssh2.default_ssh()
ssh3.call_timeout = 60  # True
ssh3.connect()
