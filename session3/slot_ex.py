from collections import namedtuple
# This is an example of slot usage
from types import MappingProxyType


service = namedtuple('Service', ('name', 'url', 'ip_attr'))

service1 = service('ipify', 'https://api.ipify.org?format=json', 'ip')
service2 = service('ip-api', 'http://ip-api.com/json', 'query')


service3 = service1._asdict()
service3['name'] = 'other'
class A:
    pass


a = A()
a.x = 66
a.y = "dynamically created attribute"

print(a.__dict__)  # The dictionary containing the attributes of "a" can be accessed like this

x = 42
#x.a = "not possible to do it"

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'a'
"""

lst = [34, 999, 1001]
#lst.a = "forget it"
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'a'
"""

class S():
    __slots__ = ['val']


x = S()
x.val = 10
print(x.val)
x.val = 50
print(x.val)


"""
42
Traceback (most recent call last):
  File "slots_ex.py", line 12, in <module>
    x.new = "not possible"
AttributeError: 'S' object has no attribute 'new'
"""