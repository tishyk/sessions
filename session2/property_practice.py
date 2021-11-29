import getpass
import time


class EmployeePassword:
    def __init__(self, first, last, expiration_time):
        self.first = first
        self.last = last
        self.__secret = hash(getpass.getpass(prompt=f"Set {first} {last} password:"))
        self.__default_password = hash('admin')
        self.__login_time = time.time()
        self.__expiration_time = expiration_time
        pass

    def login(self, expiration_time=None):
        pwd = getpass.getpass()
        if hash(pwd) == self.__secret:
            self.__login_time = time.time()
            self.__expiration_time = expiration_time if expiration_time else self.__expiration_time
            print(f"{self.first} {self.last} logged in for {self.__expiration_time} second/s")
        else:
            print("Failed to login")

    @property
    def password(self):
        if time.time() - self.__login_time <= self.__expiration_time:
            return self.__secret
        else:
            print("Session expired. Please login again")
            self.login()
            return self.password

    @password.setter
    def password(self, new_password):
        if time.time() - self.__login_time <= self.__expiration_time:
            self.__secret = hash(new_password)
            print(f"A new password was set for {self.first} {self.last}")
        else:
            print("Session expired. Please login again")
            self.login()
            self.password = new_password

    @password.deleter
    def password(self):
        if time.time() - self.__login_time <= self.__expiration_time:
            print(f"***Set default password for {self.first} {self.last}***")
            self.__secret = self.__default_password
        else:
            print("Session expired. Please login again")
            self.login()
            del self.password


corey = EmployeePassword('Corey', 'Schafer', 10)
print(corey.password)
corey.password = "demo"
del corey.password
time.sleep(11)
print(corey.password)   # admin
corey.login(expiration_time=2)
time.sleep(3)
corey.password = "demo" #admin
time.sleep(3)
del corey.password

# print(emp_1.first)
# # print(emp_2.password)
