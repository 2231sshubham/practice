def generator(num):
    for i in range(num):
        print(i)
        yield i

# for item in generator(100):
#     print(item)
a = generator(10)
next(a)
next(a)
next(a)
next(a)

