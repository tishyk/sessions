# rlock_ex.py
# An example of code-based locking.  Every method of the class
# below uses the same RLock object.  However, some methods call
# other methods.  These nested calls will work within the same
# thread.

import threading

COUNT = 1000


class Foo(object):
    lock = threading.RLock()

    def __init__(self):
        self.x = 0

    def add(self, n):
        print(threading.currentThread().name)
        with Foo.lock:
            self.x += n

    def incr(self):
        with Foo.lock:
            self.add(1) # x += 1

    def decr(self):
        with Foo.lock:
            self.add(-1) # x -= 1


# Two functions that will run in separate threads and call methods
# on the above class.

def adder(f, count):  # change to class usage
    while count > 0:
        f.incr()
        count -= 1


def subber(f, count):
    while count > 0:
        f.decr()
        count -= 1


# Create some threads and make sure it works

f = Foo()

t1 = threading.Thread(target=adder, args=(f, COUNT))
t2 = threading.Thread(target=subber, args=(f, COUNT))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done", f.x)
