def debugattr(cls):
    origin_getattribute = cls.__getattribute__

    def __getattribute__(self, name):
        print("Get attribute:", name)
        return origin_getattribute(self, name)

    cls.__getattribute__ = __getattribute__
    return cls


class DebugMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        cls_obj = super().__new__(cls, clsname, bases, clsdict)
        cls_obj = debugattr(cls_obj)
        return cls_obj


class Platform(metaclass=DebugMeta):
    def __init__(self, *args, **kwargs):
        [self.__setattr__('var{}'.format(i), var) for i, var in enumerate(args)]
        self.__dict__.update(kwargs)


platform = Platform(1, 2, 5, 8, 90, hi=True, msg="Greatings")
print(platform.msg)

# All values in Python have  a type


# How to change a metaclass from default type to any other?
# Keyword argument is - metaclass / __metaclass__
# Set the class used for creating type

class RegularClass(metaclass=type):  # it's set to type by default. You can change it to something else
    class_var = 10  # class variable

    def __init__(self, inst_var):
        self.inst_var = inst_var  # instance variable

    def inst_method(self):
        print('Inst method')  # instance method

    def __call__(self):
        pass


print(RegularClass(1000))
object1 = RegularClass(1)
object()


# We are typically inherit from type and redefine __new__ or __init__

class MClass(type):
    def __new__(cls, cls_name, bases, clsdict):
        print(f"Class {cls_name} creation")
        if len(bases) < 1:
            raise TypeError(f"Can't instantiate abstract class {cls_name}")
        clsobj = super().__new__(cls, cls_name, bases, clsdict)
        return clsobj

    def meta_method(self):
        print("Before cls object creation",
              self.__dict__)

    def __call__(self, *args, **kwargs):
        print("Class call", self.class_var)
        return super(MClass, self).__call__(*args,**kwargs)


class BaseClass(object, metaclass=MClass):  # it's set to type by default. You can change it to something else
    class_var = 10  # class variable

    def __init__(self, inst_var):
        print('BC constructor')
        self.inst_var = inst_var  # instance variable

    def inst_method(self):
        print('Inst method')  # instance method


bc = BaseClass(10)
pass

# print(BaseClass(1000))

class A(BaseClass): pass


class B(BaseClass): pass


# A.meta_method()

a = A('Hello')
# a.meta_method()  #Failed with AttributeError: 'A' object has no attribute 'meta_method'



class MetaA(type):
    def __new__(cls, *args, **kwargs):
        args[2].update({'a':"abc"})
        cls_object = super().__new__(cls, *args, **kwargs)
        return cls_object

    def __init__(self, basename, parents, clsdict):
        self.basename = basename
        print(self, basename, parents, clsdict)
        print("Class variables creation")


    def __call__(cls, *args, **kwargs):
        print("Class on call actions")
        return super().__call__(*args, **kwargs)

    def run_cls(cls):
        print('Run from metaclass')


class A(metaclass=MetaA):

    def __init__(self):
        print('Object Actions')

    def run(self):
        print("Run from simple object")

    @classmethod
    def second_run(cls):
        print("Second", cls.__dict__)


a = A()
a.run()
pass
