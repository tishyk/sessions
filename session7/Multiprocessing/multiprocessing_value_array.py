import multiprocessing

def calc_square(numbers, result, v):
    if v.value :
        for idx, n in enumerate(numbers):
            result[idx] = n*n

if __name__ == "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array('c', 3)   # str
    v = multiprocessing.Value('d', 1.0)
    p = multiprocessing.Process(target=calc_square, args=(numbers, result, v))

    p.start()
    p.join()

    print(v.value, result.value)