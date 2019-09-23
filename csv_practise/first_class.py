from functools import wraps


def decorator_func(orig_func):
    @wraps(orig_func)
    def wrapper_func(*args, **kwargs):
        print("Hello darkness my old friend")
        return orig_func("Roman")
    return wrapper_func

@decorator_func
def say_hello(*args):
    for arg in args:
     print("Hello {}".format(arg))


# class decorator_class_sum(object):
#
#     def __init__(self, orig_func):
#         self.orig_func = orig_func
#
#     def __call__(self, *args, **kwargs):
#         print("Adding items to shoplist")
#         total_sum = 0
#         for key, value in kwargs.items():
#             try:
#                 total_sum += value
#             except TypeError:
#                 continue
#         print("Total sum of items: {}".format(total_sum))
#         return self.orig_func(*args, **kwargs)
#
#
def timer_decorator(orig_func):
    import time
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = float(time.time() - t1)
        print("Function {} took {} sec.".format(orig_func.__name__, round(t2, 3)))
        return result
    return wrapper



def decorator_sum(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        total_sum = 0
        for key, value in kwargs.items():
            try:
                total_sum += value
            except TypeError:
                continue
        print("Total sum is {}".format(total_sum))
        return orig_func(*args, **kwargs)
    return wrapper


from time import sleep

@timer_decorator
@decorator_sum
def add_items(*args, **kwargs):
    my_dict = {}
    for item in args:
        #sleep(0.3)
        print("Adding {}, price: unknown".format(item))
        my_dict[item] = None
    for key, value in kwargs.items():
        #sleep(0.3)
        print("Adding {}, price: {}".format(key, value))
        my_dict[key] = value
    return my_dict

my_shit = {'Goldfish': 90, 'Dogfish': 150}
my_shit['Brownfish'] = 420

my_shit2 = ['redsocks', 'bedrock', 'shovel']

new_shit = add_items('bush', 'someshit', *my_shit2, bike = 90, plane = 100, Elonmusk = 1000, **my_shit)

print(new_shit.keys())
