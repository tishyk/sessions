class Singleton_Lazy():
    __instance = None

    def __init__(self):
        test_name = ""
        if not Singleton_Lazy.__instance:
            print("__init__ method called...")
        else:
            print("Instance already created: {}".format(self.getInstance()))

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton_Lazy()
        return cls.__instance


class Singleton_Strict(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton_Strict, cls).__new__(cls)
        return cls.instance


sl = Singleton_Lazy()
sl2 = Singleton_Lazy()
print('Lazy Singleton Instances: ')
serial1 = sl.getInstance()
serial2 = sl2.getInstance()
print(serial1, serial2)
sl3 = Singleton_Lazy()


print('Strict Singleton Instances: ')
ss = Singleton_Strict()
ss2 = Singleton_Strict()
print(ss, ss2)

