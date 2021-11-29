# lock_ex.py
# A simple example of using a mutex lock for critical sections

import threading
import time
from threading import Lock, Thread

x = 0  # A shared value
lock = Lock()  # A lock for synchronizing access to x

lock.acquire()
lock.release()

COUNT = 10


def foo(l):
    global x
    print("Started foo")
    for i in range(COUNT):
        l.acquire()
        x += 1
        print('wait from foo')
        time.sleep(5)
        l.release()


def bar():
    global x
    print("Started bar")
    for i in range(COUNT):
        with lock:
            print('wait from bar')
            x -= 1

def bar2():
    global x
    print("Started bar2")
    for i in range(COUNT):
        print('wait from bar 2')
        x -= 1



t1 = Thread(target=foo, daemon=True, args=(lock,))
t2 = Thread(target=bar)
t3 = Thread(target=bar2)
t1.start()
t2.start()  # + interval sec
t3.start()  # + interval sec
t1.join()
t2.join()
t3.join()

print(x)
