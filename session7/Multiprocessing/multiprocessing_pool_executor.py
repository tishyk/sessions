from concurrent.futures import ProcessPoolExecutor, as_completed, ThreadPoolExecutor

import time
import multiprocessing
import threading

def func(n):
    time.sleep(n)
    print(multiprocessing.current_process().name)
    print(threading.current_thread().name)
    return f'I was do this task during {n} seconds'


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as executor:
        p1 = executor.submit(func, 3)
        p2 = executor.submit(func, 5)

        # print(p1.result())
        # print(p2.result())
        for proc in as_completed((p1, p2)):
            print(f"Completed result: {proc.result()}")

