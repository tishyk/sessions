import time
import os, signal
import multiprocessing

arr = [2, 3, 8]
variables = 1,2,3,4


def calc_square(numbers):
    global variables
    for n in numbers:
        print('square ' + str(n*n))
        time.sleep(0.5)
        variables = 10

def calc_cube(numbers):
    global variables
    time.sleep(1)
    while True:
        for n in numbers:
            print('cube ' + str(n ** 3))
            time.sleep(0.3)
        break


if __name__ == "__main__":

    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
    p2.daemon = True

    time.perf_counter()
    p1.start()
    p2.start()

    p1.join()
    # p2.join()
    # print(p1.pid)
    p1.terminate()
    os.kill(p2.pid, signal.SIGTERM)
    print(p1.exitcode)

    print(p1.pid)
    print(p2.pid)
    print(f"Done in {time.perf_counter()}!")