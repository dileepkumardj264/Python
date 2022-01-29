# names = ['apple', 'ball', 'cat', 'dog']
#
#
# class Sample:
#
#     def __init__(self, iterable):
#         self.names = iterable
#         self.iter_ = iter(self.names)
#
#     def __iter__(self):
#         return iter(self.names)
#
#     def __next__(self):
#         return next(self.iter_)
#
#
# s = Sample(names)
#
# for i in s:
#     print(i)
# print(next(s))
# print(next(s))

###########################################################

# class Numbers:
#
#     def __init__(self):
#         self.start = 11
#         self.end = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start > self.end:
#             self.start -= 1
#             return self.start
#         else:
#             raise StopIteration
#
#
# n = Numbers()
#
# for i in n:
#     print(i)
#

 ##################################################################

# l = [1, 2, 3, 4]
#
# class Reverse:
#
#     def __init__(self, iterable):
#         self.m = iterable
#         self.index = len(self.m) -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == -1:
#             raise StopIteration
#         else:
#             x = self.index
#             self.index -= 1
#             return self.m[x]
#
#
# n = Reverse(l)
#
# for i in n:
#     print(i)
#

#
# n = Reverse(l)
#
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))

#########################################################


# class Even:
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start <= self.end:
#             x = self.start
#             self.start += 1
#             if x % 2 == 0:
#                 return x
#         else:
#             raise StopIteration
#
#
# s = Even(1, 20)
#
# for i in s:
#     if i:
#       print(i)

######################################################

# class Square:
#
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == len(self.iterable):
#             raise StopIteration
#         else:
#             x = self.index
#             self.index += 1
#             return self.iterable[x] ** 2
#
# n = Square([1,2,3,4])
#
# for i in n:
#     print(i)

####################################################################

# class Prime:
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.end:
#             x = self.start
#             self.start += 1
#             if x > 1:
#                 for i in range(2, x):
#                     if x % i == 0:
#                         break
#                 else:
#                     return x
#         else:
#             raise StopIteration
#
# p = Prime(1, 50)
#
# for i in p:
#     if i:
#         print(i)

#########################################################

class Fibo:

    def __init__(self,start, scno, end):
        self.start = start
        self.scno = scno
        self. end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            x = self.start
            temp = x + self.scno
            self.start = self.scno
            self.scno = temp
            return x
        else:
            raise StopIteration

f = Fibo(1, 2, 50)

for i in f:
    print(i)
