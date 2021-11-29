# event_barrier.py
#
# An example of using an event to set up a barrier synchronization

import threading
import time

event = threading.Event()
event2 = threading.Event()


def worker():
    print("I'm worker", threading.currentThread().name)
    event.wait(5)  # Wait until initialized
    print("Run", threading.currentThread().name)
    event.wait()
    print('Done')

def worker2():
    print("I'm worker", threading.currentThread().name)
    event.wait(20)
    print("Run", threading.currentThread().name)
    print('Done')



def greenlights():
    time.sleep(2)
    print("Initializing some data")
    time.sleep(10)
    print("Unblocking the workers")
    event.clear()
    print("Run all threads who wait for event")
    input()
    event.set()
    event.clear()
    time.sleep(3)
    event.set()


# Launch a bunch of worker threads
threading.Thread(target=worker).start()
threading.Thread(target=worker2, name='HI_TREAD').start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()

# Go initialize and eventually unlock the workers
greenlights()
