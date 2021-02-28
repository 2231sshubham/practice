# def some_fun(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator))
#         except StopIteration:
#             break
#
#
# some_fun([1,2,3,4,5])
# list1 = iter([1,2,3,4,5])
#
# for item in list1:
#     print(list1)
#     print(next(list1))


def fib_gen(num):
    print(0, end="\n")
    print(1, end="\n")
    a = 0
    b = 1
    for i in range(num):
        c = a + b
        print(c)
        yield
        a = b
        b = c

next(fib_gen(10))
next(fib_gen(10))
next(fib_gen(10))
next(fib_gen(10))
next(fib_gen(10))


