# countdown.py
#
# Example of launching a process with the multiprocessing module

import time
import multiprocessing
import threading
x = 0

class CountdownProcess(multiprocessing.Process):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def run(self):
        global x
        while self.count > 0:
            print("Counting down", self.count)
            self.count -= 1
            time.sleep(1)
        x = 20


if __name__ == '__main__':
    p1 = CountdownProcess(10)  # Create the process object
    p1.start()  # Launch the process

    p2 = CountdownProcess(20)  # Create another process
    p2.start()  # Launch

    [CountdownProcess(i).start() for i in range(10, 15)]