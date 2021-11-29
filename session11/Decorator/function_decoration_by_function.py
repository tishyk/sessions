
def deco(func):  # step 2
    print('before wrapper')  # Step 3.1

    def wrapper(*args):
        # step 3.2  ---------
        print('Wrapper for function {}'.format(func.__name__))
        func(*args)
        # --------

    print('after wrapper')  # Step 3.1
    return wrapper


@deco  # Step 3.1 #4
def decorated(*args):  # # step 1
    print("Inside function")
    print(*args)

class A:pass

print(callable(decorated))

decorated(1, 2, 3, "Hi decorator")  # step 3.2 # step 5   # wrapper(1, 2, 3, "Hi decorator")
# decorated(1, 2, 3, "Hi decorator")  # step 3.2 # step 5
# decorated(1, 2)  # step 3.2 # step 5

# 1. Need to have a target to wrap around  # decorated
# 2. Need to add some actions to target
# 3. Implement extra actions into decorator  # deco
# 3.1 Add action to decoration step #@deco  # Step 3.1
# 3.2 Add action to target call from decorator #@deco  # Step 3.2
# 4. Wrap a target with a decorator
# 5. Call a target # decorated
