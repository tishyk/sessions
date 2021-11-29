from abc import ABC, abstractmethod


# class Base(ABC):
#
#     # @property
#     # @abstractmethod
#     # def CONSTANT(cls):
#     #     return NotImplementedError
#     @abstractmethod
#     def print_constant(self):
#         print(type(self).CONSTANT)


# class Derived(Base):
#     CONS = 42

class Connection(ABC):
    @property
    @abstractmethod
    def IP(self):
        pass

    @property
    @abstractmethod
    def PWD(self):
        pass

    @classmethod
    @abstractmethod
    def new(cls):
        pass

    @abstractmethod
    def conect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def get_status(self):
        pass





# connection.attributes / Static variable

class SSH(Connection):
    IP = '0.0.0.0'
    PWD = "admin"

    def conect(self):
        pass

    def disconect(self):
        pass

    def close(self):
        pass

    def get_status(self):
        pass

    #@classmethod
    def new(cls):
        pass

# connection = Connection()
# connection.IP
# connection.conect()
# connection.close()
# connection.get_status()

# Connection.new(user, pwd)
# connection.new(user, pwd)

ssh = SSH()
ssh.new()
pass
# ssh.close()
