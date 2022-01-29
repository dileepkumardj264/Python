# count = 0
# d = {}
#
# def outer(func):
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         d[func.__name__] = count
#         func()
#     return inner
#
# @outer
# def add():
#     print('hai')
#
#
# @outer
# def sub():
#     print('hello')
#
#
# add()
# sub()
# add()
# print(d)

# def outer(func):
#     def inner(a):
#         res = func(a)
#         return res
#     return inner
#
# @outer
# def pos(x):
#     return abs(x)
#
#
# print(pos(-1))



import time
# def pouter(n):
#     def outer(func):
#         def inner():
#             for i in range(n):
#                 func()
#         return inner
#     return outer
#
#
#
# @pouter(3)
# def add():
#     print('hai')
#
# add()
#
#

# def outer(func):
#     def inner(*args):
#         start = time.time()
#         res = func(*args)
#         print(res)
#         end = time.time()
#         print(end-start)
#     return inner
#
#
# @outer
# def add(a, b):
#     return a + b
#
#
# add(2, 3)
#
#
# @outer
# def sub(a, b):
#     return a - b
#
#
# sub(3, 4)


# def outer(func):
#     def inner(a):
#         return func(a)
#     return inner
#
#
# @outer
# def sq(n):
#     return n**2
#
#
# print(sq(5))

#
# def outer(func):
#             def inner(*args):
#                 for i in args:
#                     if not(isinstance(i, int)):
#                         return 'invalid input'
#                 else:
#                     res = func(*args)
#                     return res
#             return inner
#
# @outer
# def add(a, b, c):
#     return a + b + c
#
#
# print(add(1, 2, 3))


# def outer(func):
#     print('hai')
#     def inner():
#         print('hello')
#         func()
#         print('im fyn')
#     print('how are you')
#     return inner
#
#
# @outer       #sam = outer(sam)     func = sam      sam = inner
# def sam():
#     print('good morning')


# print(sam())


# d = [{'a':8, 'b':2, 'c':3}, {'b':4, 'a':5, 'c':6}]
# print(sorted(d))
# print(sorted(d.items()))
# print(sorted(d.items(), key=lambda item:item[0], reverse=True))

# print(sorted(d, key=lambda item: item['a']))


# def cube(n):
#     for i in range(1,n):
#         if i>1:
#             for j in range(2,i):
#                 if i%j == 0:
#                     break
#             else:
#                 yield i**3
#
#
# res = cube(20)

# res = (True if i%j != 0 else False for i in range(2, 20) for j in range(2, i))



# l = [(), 0, set(), '', {}]
# print(all(l), any(l))
# n=11
# out = [(n % i != 0) for i in range(2,n)]
# print(all(out))
#
# prime = [num**3 for num in range(1,10) if num>1 and all([(num % i != 0) for i in range(2,num)])]
# print(list(prime))

# def sam():
#
#     yield 1
#     print('hai')
#     yield 2
#     yield 3
#
#
# res = sam()
# print(list(res))
# print(next(res))
# print(next(res))
# print(next(res))

def arm(n):
    for i in range(1, n):
        sum = 0
        for j in str(i):
            sum += int(j)**int(len(str(i)))
        if sum == i:
            yield i


res = arm(500)
print(list(res))


def prime(m):
    for n in range(1, m):
        if n>1:
            for i in range(2, n):
                if n%i==0:
                    break
            else:
                yield n


print(list(prime(100)))
