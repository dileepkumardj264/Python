# i = 1
# fac = 1
# while i <= 10:
#     fac *= i
#     print(fac)
#     i += 1
#
#
# def factorial(n, fac):
#     if n == 0:
#         return fac
#     fac *= n
#     return factorial(n-1, fac)
#
#
# print(factorial(10, 1))

# def sam(n, sum, i):
#     if i > n:
#         return sum
#     sum += i
#     return sam(n, sum, i+1)
#
#
# print(sam(10, 0, 1))

# def rev(s, res='', i=0):
#     if i == len(s):
#         return res
#     res = s[i] + res
#     return rev(s, res, i+1)
#
#
# print(rev('hello'))


# i = 0
# j = 1
# count = 10
# while count > 0:
#     print(i)
#     temp = i + j
#     i = j
#     j = temp
#     count -= 1

# def fab(count=10, i=0, j=1):
#     if count == 0:
#         return
#     print(i)
#     temp = i + j
#     i = j
#     j = temp
#     return fab(count-1, i, j)
#
#
# fab()
#

# n = 232456
# count = 0
# while n>0:
#     a = n % 10
#     count += 1
#     n = n//10
# print(count)

# def sam(n, count=0):
#     if n <= 0:
#         return count
#     n = n//10
#     return sam(n, count+1)
#
#
# print(sam(2234665))
#
#
# def san(n, i=0, count=0):
#     if i >= len(str(n)):
#         return count
#     return san(n, i+1, count+1)
#
#
# print(san(2453))

# def upp(s, res='', i=0):
#     while i >= len(s):
#         return res
#     if s[i] in 'aeiouAEIOU':
#         res += s[i]
#     return upp(s, res, i+1)
#
#
# print(upp('heioull'))

# def ivo(l, res=[], i=0):
#     if i >= len(l):
#         return res
#     if isinstance(l[i], int):
#         res.append(l[i])
#     return ivo(l, res, i+1)
#
#
# print(ivo(['hai', 24, 35]))

# def sam(n):
#     if n == 0:
#         return
#     print('bangalore')
#     return sam(n-1)
#
#
# sam(10)


# sq = lambda n: n**2
# print(sq(5))
#
# iterable = lambda s: s[-1]
# print(iterable('hai hello'))
#
# out = lambda a, b: a**2 + b**2 + 2*a*b
# print(out(2, 4))
#
# even = lambda n1: 'even' if n1 % 2 == 0 else 'odd'
# print(even(4))
#
# string = lambda s: 'palindrome' if s == s[::-1] else "not palindrome"
# print(string('mam'))


# even = lambda n: n**2
# print(list(map(even, [2, 3, 4, 5])))
#
# out = lambda n: n + 20 if n % 2 == 0 else n + 10
# print(list(map(out, [2, 3, 4, 5, 6])))
#
# sq = lambda n: n**2
# print(list(map(sq, range(1, 11))))
#
# cube = lambda m: m**3
# print(list(map(cube, range(1, 11))))

# res = lambda ele: ele[1] ** ele[0]
# # l = [1, 2, 3, 4, 4, 5, 2]
# # out = enumerate(l)
# print(list(map(res, enumerate([1, 2, 3, 4]))))
#
#
# postive = lambda n: abs(n)
# print(list(map(postive, [1, -2, -3, -4])))

# l = [1, 2, 3, 4]
# l1 = [5, 6, 7, 8]
# res = lambda a, b: a + b
# print(list(map(res, l, l1)))
#
# print(list(map(lambda a, b: a+b, [1, 2, 3, 4], [5, 6, 7, 8, 9])))

# def even(a):
#     if a % 2 == 0:
#         return a
#
#
# print(list(filter(even, [1, 2, 3, 4])))

# print(list(filter(lambda n: n % 2 == 0, [2, 3, 4, 5, 6, 7])))

# res = lambda n: n**2
# print(list(filter(res, [2, 3, 4, 5, 6])))

# l = ['hai', 'hello', 'dileep', 'four', 'five']
# print(list(filter(lambda s: len(s) % 2 == 0, l)))

# print(list(filter(lambda s: s[0] in 'aeiouAEIOU', ['apple', 'ice cream', 'elephant', 'monkey'])))
#
# print(list(filter(lambda n: n < 0, [1, -2, -3, 4, -5, -6])))
#
# def sam(n):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 return 0
#         else:
#             return 1


# prime = filter(sam, range(50))
# print(list(prime))

# def sum(l, sum=0, out=0 ):
#     for i in l:
#         if i > 0:
#             sum += i
#         else:
#             out += i
#     return sum, out
#
#
# print(sum([1, 2, -3, -4, -2]))

# pos = filter(lambda n: n > 0, [1, 2, -3, -4])
# neg = filter(lambda n: n < 0, [1, 2, 3, -4, -5])
# print(sum(pos), sum(neg))


# def sam(s, ch,res ='',):
#     l = []
#     for i, j in enumerate(s):
#         if j == ch:
#             res += j
#             if ch not in res:
#                 return i
#             else:
#                 l.append(i)
#     return l
#
#
# print(sam('hai hello how are you', 'h'))

# def fanc(name, value):
#     if value == 0:
#         print('RCN')
#     elif value == 1:
#         print('TAX')
#
#
# fanc('TRACXN', 1)


# def sam(n):
#     s = str(n)
#     return int(s[-1])
#
#
# print(sam(234))

# print(list(map(lambda n: abs(n), [1, -2, -3, -4, -5])))
# print(list(map(lambda n: n[1] ** n[0],enumerate([1,2,3,4,5,6]))))
# print(list(map(lambda n: n**2, [1,2,3,4])))
# print(list(map(lambda a, b: a+b, [1,2,3,4,6], [5,6,7,8,9,12])))
# print(list(filter(lambda n: n%2 == 0,[2,3,4,5,6])))
# print(list(filter(lambda n: n%2, [2,3,4,5,6,7])))
# print(list(filter(lambda item: len(item) % 2 == 0, ['helo', 'word', 'hai'])))

# n = 'a'
# print(list(map(lambda item: item.startswith(n), ['apple', ' ant', 'hello'])))
#
#
# print(sorted(['234', '2345', '46436'], key=len, reverse=True))
# print(list(num for num in range(1, 30) if num > 1 and all([num % i != 0 for i in range(2, num)])))

# i = 1
# count = 1
# sum = 0
# l =[]
# while count <= 10:
#     if i % 2 == 0:
#         l += [i]
#         count += 1
#         sum += i
#     i += 1
# print(sum)
# print(l)

# def sum(n):
#     if n == 1:
#         return 1
#     return n + sum(n-1)
#
#
# print(sum(10))


from collections import Counter

s = 'haihello'
d = Counter(s)
print(d)
