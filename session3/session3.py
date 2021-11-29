from collections import namedtuple

# Magic Methods:
#     __init__ method
#     __new__ method
#     Callable Objects:
#         __call__(self, [args...]) Allows an instance of a class to be called as a function
class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Child created")

    def __call__(self, *args, **kwargs):
        print("Hello from Tod", args, kwargs)


    def __iter__(self):
        return iter((self.name, self.age))

    def __setattr__(self, key, value):
        new_value = self.__dict__.setdefault(key, value)
        print(f"Set value for {key}: {new_value}")

    # def __getattribute__(self, item):
    #     # self.name
    #     # getattr(object, "attr_name")
    #     print(f'Get attribute: {item}')
    #     return super(Child, self).__getattribute__(item)

    def __getattr__(self, item):
        print(f"\tGet attr: {item}")



class Person:

    def __new__(cls, *args, **kwargs):
        if kwargs.get('age') < 18:
            obj = object.__new__(Child)
            obj.__init__(*args, **kwargs)
        else:
            obj = super().__new__(cls)
        return obj

    def __init__(self, name, age=28):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print("Hello from Tod", args, kwargs)

    def run(self):
        print("Run")

    def __ge__(self, other):  # >=
        # Comparison magic methods:
        #        __eq__(self, other): ==
        #        __ne__(self, other): !=
        #        __lt__(self, other): <
        #        __gt__(self, other): >
        #        __le__(self, other): <=
        #        __ge__(self, other): >=
        assert isinstance(other, (self.__class__, Child))
        return self.age >= other.age

    def __gt__(self, other):
        assert isinstance(other, (self.__class__, Child))
        return self.age >= other.age

    def __int__(self):
        return self.age

    def __repr__(self):
        return f"{self.__class__.__name__}: name={self.name}; age={self.age}"

        # __int__(self) Implements type conversion to int.
        # __long__(self) Implements type conversion to long.
        # __float__(self) Implements type conversion to float.
        # __complex__(self) Implements type conversion to complex.
        # __oct__(self) Implements type conversion to octal.
        # __hex__(self) Implements type conversion to hexadecimal.

        # __str__(self):
        # __repr__(self):
        # __unicode__(self):
        # __format__(self, formatstr):
        # __hash__(self):
        # __nonzero__(self):
        # __dir__(self):

    def __enter__(self):
        # Context  Managers:
        # with open(’foo.txt ’) as bar:
        # # perform some action with bar
        #
        # __enter__(self)
        # __exit__(self, exception_type, exception_value, traceback)
        self.log = open('log.txt', 'w')
        if self.name.lower() == 'tim':
            self.log = open('tim.txt', 'w')
            self.log.write("Hello from Tim\n")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.log.write(str(exc_val))

    def __add__(self, other):
        assert isinstance(other, self.__class__)
        susan = self.__class__('baby', age=0)
        susan.parents = [self, other]
        return susan

    def __delattr__(self, item):
        print(f"Delattr: {item}")
    # Controlling Attribute Access:
    #     __getattr__(self, name):
    #     __setattr__(self, name, value):
    #     __delattr__(self, name):
    #     __getattribute__(self, name):
#
# john = Person("John", age=28)  # Person class name, call class ("John", 28), "John", 28
# ted = Person("Ted", age=32)  # Person class name, call class ("John", 28), "John", 28
# janet = Person("Janet", age=32)  # Person class name, call class ("John", 28), "John", 28
# tod = Person("Tod", age=16)  # Child class name, call class ("John", 28), "John", 28
# # if callable(tod):
# #     tod('hello')
#
# if john > tod:
#     print("yes")
#
# total_age = int(john) + int(ted)
#
# with Person("Tom", age=28) as tom:
#     tom.run()
#     # tom.total
#
# susan = janet + john
# print(susan.total1)
# print(susan.total2)
# print(susan.total3)
# del john.log
#
# x = 0
#
# # f = open('filename.txt', 'w')
# # f.write("some text")
# # f.flush()
# # f.close()
# #
# # with open('filename.txt', 'w') as f:
# #     f.write("some text")
# # f.flush()
# # f.close()
# for item in susan:
#     print(item)

class ProtectedC:
    __slots__ = ['age']
    name = 'Jim'
    last = 'Total'

    def __init__(self, age):
        self.age = age

pt = ProtectedC(80)

d = {'name': 'John', 'last': 'Last', 'age': 50}
ProtectedC = namedtuple('Protected', d.keys())

pt = ProtectedC('Todd', "Last", 50)  #Enum
print(pt.name)

new_pt = pt._asdict()

service = namedtuple('Service', ('name', 'url', 'ip_attr'))
service1 = service('ipify', 'https://api.ipify.org?format=json', 'ip')
service2 = service('ip-api', 'http://ip-api.com/json', 'query')
