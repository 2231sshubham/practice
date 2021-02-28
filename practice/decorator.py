#Uses of Decorators
from time import time


def performance(fn):
    def wrap_fn(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"It took {t2-t1} s")
        return result
    return wrap_fn

# @performance
# def long_time():
#     for i in range(100000):
#         i*5
#
# @performance
# def long_time1():
#     for i in list(range(100000)):
#         i*5
#
# long_time()
# long_time1()


# Another one!!!
#
#
# user1 = {
#     'name' : "John",
#     'valid' : True
# }
# def authenticated(fn):
#     def wrap_fn(x):
#         if x['valid']:
#             fn(x)
#     return wrap_fn
#
# @authenticated
# def message_friends(user):
#     print('message has been sent')
#
# print(message_friends(user1))

@performance
def fib_gen(num):
    print(0, end="\n")
    print(1, end="\n")
    a = 0
    b = 1
    for i in range(num):
        c = a + b
        print(c)
        a = b
        b = c


fib_gen(50)