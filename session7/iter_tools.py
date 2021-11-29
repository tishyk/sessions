import itertools
import time
#
# for number in itertools.count():
#     print(number)


# for number in itertools.chain(range(10, 80), itertools.count(80, 5)):
#     print(number)
#     time.sleep(number*0.01)

# for repeated_value in itertools.repeat("repeat me", times=100):
#     print(repeated_value)
#
# #
# for infinite_cycle in itertools.cycle("abcdefg"):
#     print(infinite_cycle)
#
for generator_slice in itertools.islice(itertools.chain(range(10, 100), itertools.count(100, 5)), 200):
    print(generator_slice)
