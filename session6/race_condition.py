# race.py
# A simple example of a race condition

import threading
import time

x = 0  # A shared value

lock_object = threading.Lock()

print(lock_object.locked())
time.sleep(1)

COUNT = 100000


def foo():
    global x
    for i in range(COUNT):
        print("True")
        lock_object.acquire()  # unlocked # Locked, wait for unlock
        x += 1
        lock_object.release()


def bar():
    global x
    for i in range(COUNT):
        # lock_object.acquire()  # unlocked
        # while lock_object.locked():
        #     pass
        with lock_object:
            x -= 1


t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=bar)

t1.start()
t2.start()

t1.join()
t2.join()

print(x)
