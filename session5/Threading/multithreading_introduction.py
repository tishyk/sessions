import time
import threading

x = 0


def calc_square(numbers):
    print("calculate square numbers")
    print(threading.current_thread())  # ---> t1.getName()
    for n in numbers:
        time.sleep(3.5)
        print('square:', n * n)


def calc_cube(numbers):
    global x

    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(3.5)
        print('cube:', n * n * n)
    x = 0

#
# def calc_cube(numbers, th):
#     global x
#     print("calculate cube of numbers")
#     print(threading.current_thread().name)
#     print(th.name)
#     for n in numbers:
#         time.sleep(0.5)
#         print('cube:', n * n * n)
#     x = 0

def monitor():
    while True:
        print('*******')
        time.sleep(0.5)


arg = [2, 3, 8, 9]
t = time.time()


t1 = threading.Thread(target=calc_square, args=(arg,), name='HandleMe', daemon=False)  # thread object in the main process
t2 = threading.Thread(target=calc_cube, args=(arg,))
t3 = threading.Thread(target=monitor, daemon=False)

t1
print("Hello")
x = 25

t1.start()
t2.start()
t3.start()

time.sleep(10)

print("done in : ", time.time() - t)
print("I am done with all my work now!")
