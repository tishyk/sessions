from collections import deque
import time
text = """no separate language for database operations

very little impact on your code to make objects persistent

no database mapper that partially hides the database.

Using an object-relational mapping is not like using an object database.

almost no seam between code and database.

Relationships between objects are handled very naturally, supporting complex object graphs without joins."""


# def counter(c=1):
#     counter = c
#     print("Counter generator created")
#     while True:
#         yield counter
#         counter += 1
#         print("New counter value generated")


def mygen(incoming, c=1):
    counter = c
    for j in incoming:
        if j:
            yield counter, j
            print("One more next call")
            counter += 1


# for i in mygen(text.splitlines()):
#     print(i)

# for i in enumerate(text.splitlines(), start=1):
#     print(i)

def some_gen(n):
    while n > -5:
        # print('SG', n)
        yield n
        # yield 1
        n -= 1
    # yield 2
    # return True


def countdown_task(n, name):

    for i in range(n+1):
        print("Action in generator", name)
        yield i
        # time.sleep(0.3)


#
# for i in countdown_task(5):
#     print('Loop i:', i)
#
gen1 = countdown_task(3, "gen 1")
gen2 = countdown_task(5, "gen 2")
gen3 = countdown_task(7, "gen 3")

#
# import itertools
#
# # for i in itertools.chain(gen1, gen2, gen3):
# #     print(i)
# #
# # for rv in itertools.repeat("abc", 25):
# #     print(rv)
# for rv in itertools.cycle("abc"+"abc"[::-1]):
#     print(rv)
#
# A list of tasks to run
tasks = deque([gen1, gen2, gen3])


def scheduler(tasks):
    while tasks:
        task = tasks.popleft()
        try:
            value = next(task)
            tasks.append(task)
        except StopIteration:
            pass


scheduler(tasks)
