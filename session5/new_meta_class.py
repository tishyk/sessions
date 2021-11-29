import pprint
# # All values in Python have  a type
#
# # Metaclass get information about class definition at the time of definition
# # -- Can inspect this data
# # -- Can modify this data
# # Essentially, similar to a class decorator
# # Metaclass propagate down hierarchies
#
# x = 10
# type(x) # --> class int
#
# s = "Hello"
# type(s)     # -->class str
#
# # etc
#
#
# # Class define a new types
#
# class Dot:
#     class_var_dot = 0
#
#     def __init__(self, dot):
#         self.dot = dot
#
#
# class DashDot,(Dot,):
#     class_var_dash = 1
#
#     def __init__(self, dash):
#         self.dash = dash
#
#
# dot = Dot('.')
# type(dot)
# # The class is the type of instance created
# # The class is a callable that creates instances
#
# # Check type of int, str etc built in classes
# type(Dot)
# print(isinstance(Dot, type))  # this mean classes are instances types but created objects has base object - object
#
# # class type:
# #     pass
#
#
# print(type)  # this class creates new "type" objects
#
# # It's used while class defining
# # Consider a class DashDot
#
# dashdot = DashDot((1, 1))
# # What are it's components?
# # Name - "DashDot"
# # Base classes - (Dot)
# # Function __init__
#
# # Whats happens during class definition?
#
# # Step 1. Body of class is isolated
#
# body = """def __init__(self, dash):
#         self.dash = dash
#         """
#
# # Step 2. The class dictionary is created
#
# clsdict = type.__prepare__("DashDot", (Dot,object))
# print(clsdict)
#
# # This dictionary serves as local namespace for statements in the class body
# # It's a simple dictionary by default
#
# # Step 3: Body is executed in returned dict (clsdict)
#
# exec(body, globals(), clsdict)  # clsdict population here
# print(clsdict)
#
# # Step 4. Class is constructed from it's name, base classes, and the dictionary
#
# DashDot = type("DashDot", (Dot,), clsdict)
# dashdot2 = DashDot((0, 0))
# print(dashdot2)


# How to change a metaclass from default type to any other?
# Keyword argument is - metaclass / __metaclass__

GLOBAL_VAR = 10

class MyMetaClass(type):
    class_var = 20

    def __new__(cls, cls_name, bases, clsdict):   # __new__(cls, *args, **kwargs)
        print(f"Class {cls_name} creation")
        if len(bases) < 1:
            raise TypeError(f"Can't instantiate class {cls_name}")
        clsdict['obj_var2'] = 20
        clsobj = super().__new__(cls, cls_name, bases, clsdict)
        return clsobj  # DashDot

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print(f"Class instance creation: {args}; {kwargs}")
        return super().__call__(*args, **kwargs)

    def run(self):
        print(f"C: Run {self}", self.obj_var) #MyClass

    @property
    def attr(self):
        return "Class attribute"

    @classmethod
    def cls_method(cls):
        return "Class method"

# MyMetaClass.open_connection()
class MyClass(object, metaclass=MyMetaClass):
    obj_var = 10
    attr = 10

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, param):
        self.param = param

    def run(self):
        print(f"O: Run {self}")

    def open_connection(self):
        pass




inst = MyClass(1001)
# inst.run()
pprint.pprint(inst.__dict__)
pprint.pprint(MyClass.__dict__)
pprint.pprint(MyMetaClass.__dict__)


x = 0