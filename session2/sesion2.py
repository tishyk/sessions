# __class__, __name__ and __doc__ variables +

class Grabber:
    def __init__(self):
        self.name = 'some name'
        self._user = 'username'
        self.__password = 'password'

    def show(self):
        print(self.__password)


gr = Grabber()
print(gr._Grabber__password)

print(gr)

