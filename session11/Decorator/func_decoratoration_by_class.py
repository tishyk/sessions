# Basic example of decorator defined by class

class Decorator():

    def __init__(self, func):
        # Step 3.1
        print('before wrapper')
        self.func = func
        print('after wrapper')
        self.cache = {}
        # ---------

    def __call__(self, *args):
        # step 3.2  ---------
        print('Called {func} with args: {args}'.format(
            func=self.func.__name__, args=args))
        print(self, args)
        return self.cache.setdefault(str(args), self.func(*args))
        # -----------------


# o = Decorator()
# my_func = o
# my_func(a1) --> o(a1)  --> __call__(a1)


@Decorator
def my_func(x, y):
    print('Function called')
    return x, y


if __name__ == '__main__':
    # Basic example of decorator defined by class
    x = my_func(1, 2)
    y = my_func(1, 2)
    z = my_func(1, 3)
    z = my_func(1, 3)

# 1. Need to have a target to wrap around  # my_func
# 2. Need to add some actions to target
# 3. Implement extra actions into decorator  # Decorator
# 3.1 Add action to decoration step #@Decorator  # Step 3.1
# 3.2 Add action to target call from decorator #@Decorator  # Step 3.2
# 4. Wrap a target with a decorator
# 5. Call a target # my_func
