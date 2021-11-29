def decorator(cls):
    # step 3.1
    print('1 - 3.1')
    class Wrapper(object):
        def __init__(self, *args):
            self.wrapped_cls = cls(*args)

        def __getattr__(self, name):
            # Step 3.2
            print('Getting the {} of {}'.format(name, self.wrapped_cls))
            return getattr(self.wrapped_cls, name)

    print('2 - 3.1')
    return Wrapper



@decorator
class C(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_color(self):
        print("Set color")


if __name__ == '__main__':
    x = C(1, 2)
    print(x.x)
    x.set_color()

# 1. Need to have a target to wrap around  # my_func
# 2. Need to add some actions to target
# 3. Implement extra actions into decorator  # Decorator
# 3.1 Add action to decoration step #@Decorator  # Step 3.1
# 3.2 Add action to target call from decorator #@Decorator  # Step 3.2
# 4. Wrap a target with a decorator
# 5. Call a target # my_func
