# countdown2.py
# An example of launching a function into a separate thread
import threading

import time
from threading import Thread, Timer


def countdown(count, t=None):
    while count > 0:
        print("Counting down", count)
        count -= 1
        time.sleep(1)
    if t:
        t.join()
    print(f"Done thread name: {threading.current_thread().name}")
    return 1


# Sample execution
t1 = Thread(target=countdown, args=(10,), name="Carl")
t2 = Thread(target=countdown, args=(5, t1), daemon=False, name="John")
t1.start()
t2.start()

t1.join()
t2.join()

print('Done MainThread')

"""
Counting down 5
Counting down 4
Counting downCounting down 3
Counting down 2Done MainThread
Counting down 
1
Done thread name: Carl
 
Process finished with exit code 0
"""