import time
import multiprocessing
import signal
import os


def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()  # remove lock for example
        balance.value = balance.value + 20
        lock.release()


def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 10
        lock.release()


if __name__ == '__main__':
    balance = multiprocessing.Value('i', 0)

    lock = multiprocessing.Lock()

    d = multiprocessing.Process(target=deposit, args=(balance, lock))
    w = multiprocessing.Process(target=withdraw, args=(balance, lock))

    d.start()
    w.start()
    d.join()
    # os.kill(d.pid, signal=signal.CTRL_C_EVENT)
    w.join()
    print(balance.value)
