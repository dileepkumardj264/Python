# def spam(func):
#     def wrapper():
#         print("hello everyone")
#         func()      # display()
#     return wrapper
#
#
# @spam       # display = spam(display)
# def display():
#     print(1 + 2)
#
#
# @spam       # display2 = spam(display2)
# def display2():
#     print(1 - 2)
#

# display = spam(display)     # func = display , display = wrapper
# display()
# display2 = spam(display2)
# display2()                  # func = display2, display2 = wrapper


#######################################################################
# log decorator

# import time
#
# d = {}
# # using normal dictionary
# def log(func):
#     def wrapper(*args, **kwargs):
#         f_name = func.__name__
#         if f_name not in d:
#             d[f_name] = 1
#         else:
#             d[f_name] += 1
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# # using default dictionary
# from collections import defaultdict
# dd = defaultdict(int)
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         f_name = func.__name__
#         dd[f_name] += 1
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# # using count
# d = {}
# def log(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         f_name = func.__name__
#         nonlocal count
#         count += 1
#         d[f_name] = count
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
#
# @log     # @log
# def add(a, b, c):
#     return "adding 2 numbers:", a + b + c
#
#
# @log
# def sub(a, b):
#     return a - b


# print(add(1, 2, c=3))
# print(add(1, 2, c=3))
# print(add(1, 2, c=3))
#
# print(sub(3, 9))
# print(sub(3, 9))
#
# # {add: 3, sub: 2}
# print(d)

###########################################################################
# def n_times(n):
#     def repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 res = func(*args, **kwargs)
#                 print(res)
#         return wrapper
#     return repeat
#
# @n_times(3)
# def add(a, b):
#     return a + b
#
# @n_times(2)
# def sub(a, b):
#     return a - b
#
# add(11, 2)
# sub(3, 1)
#

#######################################################################
from _ast import arg

import time
# def spam():
#     return "hello"
#
# start = time.time()
# print(start)
# time.sleep(3)
# print(spam())
# time.sleep(3)
# end = time.time()
# print(end)
# print(end - start)


""" assignment 

@ type_check(int, int, int)
def add(a, b, c):
    return a + b

add(1, 2, 3)
add("hai", 1, 2)

"""

# def sq():
#     print(sq.__name__)
#     print(3**2)
#
#
# sq()


# def outer(func):
#     def inner(s):
#         res = func(s)
#         return res[::-1]
#     return inner
#
#
# @outer
# def rev(a):
#     return a
#
#
# print(rev('hai'))
#
# def outer(func):
#     def inner(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(len(args) + len(kwargs))
#         return res
#     return inner
#
#
# @outer
# def sam(a, b, c, d=0, e=0):
#     return a + b + c + d + e
#
#
# print(sam(1, 2, 3, d=6, e=7))


# def validate(*type_):
#     def outer(func):
#         def wrapper(*args):
#             for i, j in zip(args, type_):
#                 if not(isinstance(i, j)):
#                     return f'{i} is not of type{j}'
#                 else:
#                     print(f'{i} is of type {j}')
#             else:
#                 res = func(*args)
#                 return res
#         return wrapper
#     return outer
#
#
# @validate(int, str, int)
# def add(a, b, c):
#     return str(a) + b + str(c)
#
#
# print(add(2, '3', '4'))

#########################################################

# def outer(func):
#     def wrapper(*args):
#         for i in args:
#             print(abs(i))
#         res = func(*args)
#         return res
#     return wrapper
#
#
# @outer
# def add(a, b, c):
#     return a + b + c
#
#
# print(add(2, -3, -5))


# def outer(func):
#     def wrapper(*args):
#         for i in args:
#             if i > 1:
#                 for j in range(2, i):
#                     if i % j == 0:
#                         print(f'{i}, not a prime')
#                         break
#                 else:
#                     print(f'{i}, is a prime number')
#         res = func(*args)
#         return res
#     return wrapper
#
# @outer
# def add(a, b, c):
#     return a + b + c
#
#
# print(add(2, 3, 4))


from collections import defaultdict
d = defaultdict(int)

class Count:

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            fname = func.__name__
            d[fname] += 1
            func(*args, **kwargs)
        return wrapper

@Count()
def add(a, b, c):
    print(a + b + c)


@Count()
def sub(a, b):
    print(a - b)

add(2,3,4)
add(4,5,6)
sub(5,2)

print(d)
