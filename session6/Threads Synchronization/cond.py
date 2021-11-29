# cond.py
#
# An example of using a condition variable to set up a producer/consumer
# problem.

import threading
import time

# A list of items that are being produced.
# Note: it is actually more efficient to use a collections.deque() object for this.

items = []

# A condition variable for items
items_cv = threading.Condition()


# A producer thread
def producer():
    print("I'm the producer")
    for i in range(20):
        with items_cv:  # Always must acquire the lock first
            items.append(i)  # Add an item to the list
            print(f"Generate number {i}")
            items_cv.notify()  # Send a notification signal
            time.sleep(0.5)


# A consumer thread
def consumer():
    print("I'm a consumer", threading.currentThread().name)
    while True:
        with items_cv:  # Must always acquire the lock
            items_cv.wait()  # If not, we have to sleep
            x = items.pop(0)  # Pop an item off

        print(threading.currentThread().name, "got", x)



# Launch a bunch of consumers
cons = [threading.Thread(target=consumer) for i in range(5)]
# Run the producer
prod = threading.Thread(target=producer)

prod.start()
for c in cons:
    # c.setDaemon(True)
    c.start()


