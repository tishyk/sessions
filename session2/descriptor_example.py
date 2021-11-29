import logging

logging.basicConfig(level=logging.INFO)

# Example 1
class LoggedAgeAccess:

    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value

class INT:
    def __set__(self, instance, value):
        assert isinstance(value, int), "Wrong value type"
        assert value > 12 and value < 130, "Wrong age"
        instance.__dict__['age'] = value
        instance.__dict__['my_age'] = value



class Person:

    age = INT()             # Descriptor instance

    def __init__(self, name, age):
        self.name = name                # Regular instance attribute
        self.age = age                  # Calls __set__()

    def birthday(self):
        self.age += 1

# Example 2
# class LoggedAccess:
#
#     def __set_name__(self, owner, name):
#         self.public_name = name
#         self.private_name = '_' + name
#
#     def __get__(self, obj, objtype=None):
#         value = getattr(obj, self.private_name)
#         logging.info('Accessing %r giving %r', self.public_name, value)
#         return value
#
#     def __set__(self, obj, value):
#         logging.info('Updating %r to %r', self.public_name, value)
#         setattr(obj, self.private_name, value)
#
# class Person:
#
#     name = LoggedAccess()                # First descriptor instance
#     age = LoggedAccess()                 # Second descriptor instance
#
#     def __init__(self, name, age):
#         self.name = name                 # Calls the first descriptor
#         self.age = age                   # Calls the second descriptor
#
#     def birthday(self):
#         self.age += 1

person = Person("John", 50)
