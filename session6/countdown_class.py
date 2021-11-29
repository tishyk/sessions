# countdown.py
# An example of defining a thread as a class

import time
import threading


class CountdownThread(threading.Thread):
    result = True

    def __init__(self, count, name, t_to_sync=None, daemon=False):
        threading.Thread.__init__(self, name=name, daemon=daemon)
        self.count = count
        self.t = t_to_sync
        self.result = False
        self.trace = False

    def join(self, timeout=None):
        super().join()
        return self.trace

    def start(self):
        super(CountdownThread, self).start()
        return self.result

    def run(self):
        try:
            print(threading.current_thread().getName())
            while self.count > 0:
                print("Counting down", self.count)
                self.count -= 1
                time.sleep(1)
            # while True:
            #     if self.t and not self.t.is_alive():
            #         print(self.t.is_alive(),
            #               self.t.name)
            #         #self.t.setDaemon(True)
            #         break
            #     print("Counting down", self.count)
            #     self.count -= 1
            #     time.sleep(0.2)
            self.result = True
            self.trace = True
            return self.count
        except Exception as exec:
            time.sleep(1)
            self.trace = exec



# Sample execution
t1 = CountdownThread(5, "Name")
t2 = CountdownThread(10, "Thread", t1, daemon=True)
t1.setDaemon(True)

initial_res1 = t1.start()
initial_res2 = t2.start()


trace1 = t1.join()
trace2 = t2.join()

print("Done", t1.result, trace1, trace2)
