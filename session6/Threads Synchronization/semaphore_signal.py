# semaphore_signal.py
#
# The example of using a semaphore to signal

import threading
import time

# semaphore = threading.Semaphore(1)
semaphore = threading.Semaphore(1)  # Number of the threads
item = []


def producer():
    global item
    print("I'm the producer and I produce data.")
    with semaphore:
        item.append("Hello")
        x = 5
        while x >= 0:
            print(x)
            x -= 1
            time.sleep(1)
        print("Producer is alive. Signaling the consumer.")

def consumer():
    print("I'm a consumer and I wait for data.")
    semaphore.acquire()  # lock.acquire()
    item.append('Hi')
    print("Add")
    time.sleep(1)
    print(f"Consumer {item} got")
    semaphore.release()     # lock.release()

t1 = threading.Thread(target=producer)

t2 = threading.Thread(target=consumer)
t3 = threading.Thread(target=consumer)
t4 = threading.Thread(target=consumer)
t5 = threading.Thread(target=consumer)


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
print('Done!')
