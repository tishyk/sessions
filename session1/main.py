from session1 import func3, d

def custom_run(self, run):
    print('Custom run', self.USER)

class TechData:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        print(self.key)


class Grabber:
    USER = 'username'
    PASSWD = "admin"

    def __init__(self):
        self.USER = 'username'
        # self.PASSWD = None
        self.__class__.PASSWD = 'se-admin'
        self.check_connection('test')
        self.set_passwd('se-admin')


    def run(self, value):
        # self.__class__.PASSWD = 'se-admin'
        print(value, self.USER)

    @classmethod
    def set_passwd(cls, pwd):
        cls.PASSWD = pwd

    @staticmethod
    def check_connection(server):
        print(f'{server} connected')

    # def set_passwd(cls, pwd):
    #     cls.PASSWD = pwd


if __name__ == "__main__":
    func3(10, 20, 0)
    print(__file__, __name__)
    #1  Grabber.PASSWD  1 admin, 2 se-admin, 3 se-admin
    Grabber.check_connection('prod')
    Grabber.set_passwd('default')
    gr = Grabber()
    gr.set_passwd('pass')
    #2  Grabber.PASSWD
    #3 gr.PASSWD = 'admin'
    #4 Grabber.PASSWD

    #getattr, setattr, delattr   built - in functions
    x1 = getattr(gr, 'USER')  # 'username'
    x2 = getattr(Grabber, 'USER')  # 'username'

    y1 = getattr(gr, 'run')  # run
    y2 = getattr(Grabber, 'run')  # run

    setattr(Grabber, 'custom_run', custom_run)

    tdata = TechData(**d)
    print(tdata.key)
    print(tdata.name)
    print(tdata.spdx_id)
    print(tdata.node_id)
    print(tdata.url)

# >>> Grabber
# <class '__main__.Grabber'>
# >>> Grabber.USER
# 'username'
# >>> Grabber.USER = "admin"
# >>> Grabber.USER
# 'admin'
# >>> gr = Grabber()
# >>> gr.USER
# 'username'
