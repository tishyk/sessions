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

    def call(self, cmd):
        print(cmd)

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

    @staticmethod
    def get_connection(**kwags):
        if kwags.get('com'):
            print("Warning! Serial conenction paramater found. Serial connection created instead of SSH")
            return Serial.get_connection(com=kwags.get('com'))
        return SSH('admin', 'admin', '192.168.0.1')


class Serial:
    def __init__(self, user: str, pwd: str, com: str):
        self.user = user
        self.pwd = pwd
        self.com = com
        self.set_defaults()

    def set_defaults(self):
        self.connected = False
        self.call_timeout = 60
        self.com = 1

    def call(self, cmd):
        print("serial:" , cmd)

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    @staticmethod
    def get_connection():
        user, pwd, com = 'admin', 'admin', 'COM1'
        return Serial(user, pwd, com)

ssh = SSH('admin', 'admin', '192.168.0.1')
serial = Serial('admin', 'admin', 'COM1')
ssh.connect()
serial.connect()

ssh.call('ls -l')
serial.call('ls -la')
ssh.call('ls')
serial.call('ls -l')
ssh.call('ls -la')
serial.call('ls')
ssh.close()
serial.close()

