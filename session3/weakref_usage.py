import sys
import random
import gc
from weakref import getweakrefcount, ref, proxy, WeakValueDictionary


"""
Not all objects can be weakly referenced; those objects which can include class instances,
 functions written in Python (but not in C), instance methods, sets, frozensets, some file objects,
  generators, type objects, sockets, arrays, deques, regular expression pattern objects, and code objects.

Changed in version 3.2: Added support for thread.lock, threading.Lock, and code objects.

Several built-in types such as list and dict do not directly support weak references
 but can add support through subclassing:

class Dict(dict):
    pass

obj = Dict(red=1, green=2, blue=3)   # this object is weak referencable
"""

class WRObject():
    def __init__(self, idx=0):
        self.demo = True
        self.idx = idx
        self.name = 'Book Name'

wr_object = WRObject()

print(sys.getrefcount(wr_object),
      getweakrefcount(wr_object))

# objects = []
# objects.append(wr_object)

print(sys.getrefcount(wr_object),
      getweakrefcount(wr_object))


def callback(wr_o):
    print("Calling callback function for destroyed object")


weak_ref_to_wr_object = ref(wr_object, callback)


# print(sys.getrefcount(wr_object),
#       getweakrefcount(wr_object))
#
# lst = [weak_ref_to_wr_object]

# del wr_object

"""
The original object can be retrieved by CALLING the reference object if the referent is still alive;
if the referent is no longer alive, calling the reference object will cause None to be returned.
"""
# print(lst)
# #
# weak_ref_to_wr_object().demo = "hello"
# print(weak_ref_to_wr_object().demo)

wr_object_proxy = proxy(wr_object, callback)

wr_object_proxy.demo = False
print(wr_object_proxy.demo)

# print(sys.getrefcount(wr_object),
#       getweakrefcount(wr_object))

wvdict = WeakValueDictionary()
wvdict['wr_object_label'] = wr_object
#
# print(sys.getrefcount(wr_object),
#       getweakrefcount(wr_object))
#
# del wr_object
#
# pass
# real_initial_values = [WRObject(i) for i in range(100)]
# weak_initial_values = [proxy(realobject) for realobject in real_initial_values]
#
#
# for wv in weak_initial_values:
#     if wv:
#         print(wv.idx)
        # real_initial_values.pop(-1)

#
#
# real_books = [WRObject(i) for i in range(1000)]
# books = WeakValueDictionary()
# books.update({book.idx:book for book in real_books})
#
# for book in books:
#     print("Book id:", book, books.get(book).name)
# pass
#
