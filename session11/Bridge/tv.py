"""Bridge pattern explanation. Abstraction"""
import abc

import samsung_tv
import lg_tv


class TV:
    """Here is an abstraction of some TV"""

    def __init__(self, tv):
        self.tv = tv()

    def power_on(self):
        print('Power on TV')
        self.tv.power_on()

    def power_off(self):
        print('Power off TV')
        self.tv.power_off()

    def volume_up(self):
        print('Volume up')
        self.tv.increase_volume()

    def volume_down(self):
        print('Volume down')
        self.tv.decrease_volume()

    def chanel_up(self):
        print('Channel up')
        self.tv.next_channel()

    def chanel_down(self):
        print('Channel down')
        self.tv.prev_channel()


# Client choose TV type
client_tv = TV(samsung_tv.UE55NU7090UXUA)

client_tv.power_on()
client_tv.chanel_up()
client_tv.chanel_up()
client_tv.chanel_down()
client_tv.volume_up()
client_tv.volume_up()
client_tv.power_off()


class ABCUser(abc.ABC):
    @abc.abstractmethod
    def set_config(self):
        pass

    @abc.abstractmethod
    def check_target(self):
        pass

    @abc.abstractmethod
    def teardown(self):
        pass

    @abc.abstractmethod
    def teardown(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass


class User1(ABCUser):
    def __init__(self):
        self.name = "user1_tech"
        self.config = "user1_tech"
        self.target = "API"

    def set_config(self):
        print("Set config for user1")

    def check_target(self):
        print("Check target for user1")

    def teardown(self):
        print("Teardown call for user1")

    def run(self):
        print("Run test for user1")


class User2(ABCUser):
    def __init__(self):
        self.name = "user1_tech"
        self.config = "user1_tech"
        self.target = "API"

    def set_config(self):
        print("Set config for user1")

    def check_target(self):
        print("Check target for user1")

    def teardown(self):
        print("Teaddown call for user1")

    def run(self):
        print("Run test for user1")


# Abstract test

class RestTest:
    def __init__(self, target):
        if target.startswith('user1'):
            self.target = User1()
        if target.startswith('user2'):
            self.target = User2()

    def setup(self):
        # setup actions
        self.target.set_config()
        self.target.check_target()

    def teardown(self):
        # cleanup methods
        self.target.teardown()

    def run(self):
        # Abstart test run
        self.target.run()


my_test = RestTest('user1')

my_test.setup()
my_test.run()
my_test.teardown()
