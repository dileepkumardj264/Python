#WAP to print first 10 even number

# i = 0
# count = 0
# while count < 10:
#     if i % 2 == 0:
#         print(i)
#         count += 1
#     i +=1

# WAP to print first 10 prime numbers
# i = 2
# count = 0
# while count < 10:
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')
#         count += 1
#     i += 1


# WAP to print even and odd numbers
# l1 = []
# l2 = []
# for i in range(20):
#     if i % 2 == 0:
#         l1 += [i]
#     else:
#         l2 += [i]
# print(l1,l2)

# WAP to print prime numbers from 1 to 30

# for n in range(2,31):
#     for i in range(2,n):
#         if n % i == 0:
#             break
#     else:
#         print(n)

# WAP to print numbers from -10 to -1

# i = -10
# while i < 0:
#     print(i)
#     i +=1

# WAP to print ASCII values of each character ina string

# s = 'haihello'
# for i in s:
#     print(ord(i))

# WAP to check whether a character is vowel or not and swap its case in the sentence

# s = 'hAi goOd morning'
# out = ''
# for i in s:
#     if i.lower() in 'aeiou':
#         if 'a' <= i <= 'z':
#             out += chr(ord(i)-32)
#         elif 'A' <= i <= 'Z':
#             out += chr(ord(i)+32)
#     else:
#         out += i
# print(out)

# i = 2
# while i < 31:
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#     i += 1

# for i in range(-10,0):
#     print(i)

# s = 'haihello'
# i = 0
# while i < len(s):
#     print(ord(s[i]))
#     i+=1

# s = 'hAi goOd morning'
# i = 0
# out = ''
# while i < len(s):
#     if s[i].lower() in 'aeiou':
#         if 'a' <= s[i] <= 'z':
#             out += chr(ord(s[i])-32)
#         else:
#             out += chr(ord(s[i])+32)
#     else:
#         out += s[i]
#     i +=1
# print(out)

# t = ('hai', 'hello', 'dileep', 'ram')
# l = list(t)
# l.sort(key=len)
# if len(t) > 3:
#     print(l[-1])

# print numbers from 1 to 4
# i = 0
# while i <= 4:
#     print(i)
#     i +=1
#
# for i in range(5):
#     print(i)

# print every alternate number st from 0

# for i in range(0, 20, 2):
#     print(i)
#
# i = 0
# while i < 20:
#     print(i)
#     i += 2

# print Numbers from 10 to 1

# for i in range(10,0,-1):
#     print(i)
#
# i = 10
# while i > 0:
#     print(i)
#     i-=1

# to print 10 to 0

# for i in range(10,-1,-1):
#     print(i)

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1

# TO PRINT 10 T0 -1

# for i in range(10,-2,-1):
#     print(i)

# i = 10
# while i >= -1:
#     print(i)
#     i -= 1

# WAP to print string 5 times
# s = 'hello'
# i = 0
# while i < 5:
#     print(s)
#     i += 1

# for i in range(5):
#     print(s)

# WAP tp print alternate number from 10 to 0

# for i in range(10,-1,-1):
#     if i % 2 == 0:
#         print(i)

# Iterate over the iterables only if the iterable has one item else add an item to the iterable

# s = 'hai'
# if len(s) >= 1:
#     for i in s:
#         print(i)
# else:
#     s += 'hello'
#     print(s)

# l = []
# if l:
#     for i in l:
#         print(i)
# else:
#     l.append('dileep')
#     print(l)

# s = {1,2,3}
# if bool(s):
#     for i in s:
#         print(i)
# else:
#     s.add('hello')
#     print(s)

# d = {'a': 1, 'b': 2}
# if d:
#     for i in d:
#         print(i, d[i])
# else:
#     d['c'] = 3
#     print(d)

# t = ()
# if t:
#     for i in t:
#         print(i)
# else:
#     t += tuple('112')
#     print(t)

# i = 0
# sum = 0
# count = 0
# while count < 10:
#     if i % 2 == 0:
#         sum += i
#         count += 1
#     i +=1
# print(sum)

# s = 'haihello'
# out = ''
# for i in s:
#     if i.islower():
#         out += i.upper()
#     else:
#         out += i
# print(out)

# s = 'HaiHeLLo'
# out = ''
# i = 0
# while i < len(s):
#     if 'A' <= s[i] <= 'Z':
#         out += chr(ord(s[i])+32)
#     else:
#         out += s[i]
#     i += 1
# print(out)

# d = {'hai', 'hello', 10, '123', 12, 90}
# for i in d:
#     if isinstance(i, (int, float)):
#         print(i)

# s = 'python selenium'
# # for i in s:
# #     if i.lower() in 'aeiou':
# #         print(i)
#
#s = 'python selenium'
# for i in s:
#     if i.lower() not in 'aeiou':
#         print(i)


# for i in range(1, 1000):
#     sum = 0
#     s = str(i)
#     for j in s:
#         sum += int(j) ** len(s)
#     if sum == i:
#         print(i)

# for i in range(1, 1000):
#     fac = 1
#     for j in range(2, i):
#         if i % j != 0:
#             break
#         else:
#             fac *= j
#     if fac == i:
#         print(i)

# import calendar
# print(calendar.isleap(2012))

# i = 1
# while i <= 1000:
#     sum = 0
#     for j in str(i):
#         sum += int(j) ** len(str(i))
#     if sum == i:
#         print(i)
#     i += 1

# i = 1
# while i <= 1000:
#     fac = 1
#     for j in range(2, i):
#         if i % j != 0:
#             break
#         else:
#            fac *= j
#     if fac == i:
#         print(i)
#     i += 1

# WAP to print only the vowels in the string along with their index.
# a = 'hello'
# for index, item in enumerate(a):
#     if item.lower() in 'aeiou':
#         print(index, item)
#
# for i in range(len(a)):
#     if a[i].lower() in 'aeiou':
#         print(i, a[i])

# WAP to print keys in a dict
# d = {'a': 1, 'b': 2, "c": 3}
# for key in d:
#     print(key)

# for key in d:
#     print(d[key])
#
# for value in d.values():
#     print(value)
#
# for key, value in d.items():
#     print(value)

# a = 'hai'
# for i in reversed(a):
#     print(i, end='')

# l = [1,2,3]
# p = [3,4,5,6]
# from itertools import zip_longest
# print(list(zip_longest(l, p, fillvalue= 'hai')))

# s = 'hello'
# m = dict(enumerate(s))
# print(m)

# s = 'hello'
# d = {}
# for index, item in enumerate(s):
#     d[index] = item
# print(d)

# for i in range(len(s)):
#     d[i] = s[i]
# print(d)


# l = [12,3,4,5,8]
# m = []
# for index, item in enumerate(l):
#     m += [item ** index]
# print(m)

# d = {}
# s = 'helloworld'
# for index, item in enumerate(s):
#     a = s.count(item)
#     d[item] = a
# print(d)
#
# for i in range(len(s)):
#     a = s.count(s[i])
#     d[s[i]] = a
# print(d)

# for i in range(len(s)):
#     if s[i] in d:
#         d[s[i]] += 1
#     else:
#         d[s[i]] = 1
# print(d)

# n = 239
# s = str(n)
# if int(s[-1]) % 3 == 0:
#     print('divisible by 3')


# s = 'sony123pvt45ltd76'
# for i in s:
#     if i.isdigit():
#         print(i)


# i = 0
# while i < len(s):
#     if s[i].isdigit():
#         print(s[i])
#     i += 1

# i = 0
# sum = 0
# while i < len(s):
#     if s[i].isdigit():
#         sum += int(s[i])
#     i += 1
# print(sum)

# s = 'hello123456'
# i = len(s) -1
# while i >= 0:
#     print(s[i])
#     i += -1

# for i in s[::-1]:
#     print(i)
#
# for i in reversed(s):
#     print(i)

# c = 0
# for i in s:
#     if i.isdigit():
#         c += 1
# print(c)

# s1 = 'hai'
# s2 = 'bye'
# # print(list(zip(s1, s2)))
# for i, j in zip(s1, s2):
#     print(i, j)

# s1 = 'hai world'
# s2 = 'bye hello'
# for i, j in zip(s1, s2):
#     if i in 'aeiouAEIOU' or j in 'aeiouAEIOU':
#         print(i, j)

# s = 'helloworld'
# for index, item in enumerate(s):
#     if index % 2 != 0:
#         print(index, item)

# l = ['apple', 'google', 'mam','flipkart', 'walmart', 'Amazon','dad']
# for index, item in enumerate(l):
#     if len(item) % 2 == 0:
#         print(item, index)

# for i in l:
#     if i[0] in 'aeiouAEIOU':
#         print(i)

# for i in l:
#     if i == i[::-1]:
#         print(i)
# m = []
# for i in l:
#     if len(i) % 2 == 0:
#         m += [i]
#     else:
#         m += [i[::-1]]
# print(m)


# l = ['hai', 2, 4, 56, 'hello', 2.5, 2+3j]
# for i in l:
#     if not (isinstance(i, str)):
#         print(i)

# l = ['facebook', 'gmail', 'yahoo']
# for i in l:
#     filename, ext = i.split('.')
#     print(ext)
# m = []
# for i in l:
#     m.insert(len(m), (i, len(i)))
# print(m)

# t = tuple(l)
# print(max(t, key=len))

# m = [1, 2, 3, 4]
# n = ['a', 'b', 'c', 'd']
# print(list(zip(n, m, l)))

# for i in l:
#     m.append((i[0], i))
# print(m)
#

# d = {'a': 'apple', 'b': 'ball', 'c': 'cat'}
# for index, (key, value) in enumerate(d.items()):
#     print(index, key, value)

# l1 = ['a', 'b', 'c']
# l2 = ['apple', 'ball', 'cat']
# d = {}
# for key, value in zip(l1, l2):
#     d[key] = value
# d = dict(zip(l1, l2))
# print(d)

# m = {}
# for k, v in d.items():
#     m[v] = k
# print(m)

# s = 'hello'
# d1 = {}
# for i in s:
#     if i not in d1:
#         d1[i] = 1
#     else:
#         d1[i] += 1
# print(d1)

# s = 'haihellooa'
# d1 = {}
# for i in s:
#     if i in 'aeiouAEIOU':
#       if i not in d1:
#           d1[i] = 1
#       else:
#           d1[i] += 1
# print(d1)
#
# s = 'aeiou'
# from collections import defaultdict
# d1 = defaultdict(int)
# for i in s:
#     if i in "aeiouAEIOU":
#         d1[i] += 1
# print(d1)

# for i in s:
#     if i in 'aeiouAEIOU':
#         d1[i] = s.count(i)
# print(d1)

#####################################
s = 'Python is a Programming language'
l = s.split()
from collections import defaultdict
d = defaultdict(list)
for i in l:
    if i.startswith(i[0]):
        d[i[0]] += [i]
print(d)

##################################
# for i in l:
#     d[i[0]] += [i]
# print(d)

##################################
# d = {}
# for i in l:
#     if i[0] not in d:
#         d[i[0]] = [i]
#     else:
#         d[i[0]].append(i)
# print(d)
#
####################################

# print([i*i for i in [1, 2, 3, 4]])
# print([i for i in range(1, 50) if i % 2 == 0])
# s = 'Apple is the only fruit good for health'
# l = s.split()
# print([i for i in l if i[0] in 'aeiouAEIOU'])
# print([i for i in l if len(i) % 2 == 0])

# l = ['python', 'java', 'perl', 'php', 'python', 'jsa', 'c++']
# print([i for i in l if i.startswith('p')])
# print([i if len(i) % 2 == 0 else i[::-1] for i in l])
# print([(i, len(i)) for i in l if len(i) % 2 != 0])
# print([i.upper() for i in l])

# print({i: len(i) for i in l})

# s = 'helloworld'
# print({i: s.count(i) for i in s})
#
# print({i: ord(i) for i in s})
#
# a = ['hai','word', 'are', 'you']
# b = [1, 2, 3, 4]
# print({i: j for i, j in zip(a, b)})
# print({i: j for i, j in enumerate(a)})
# d = {}
# for i in a:
#     if len(i) % 2 == 0:
#         d[i] = i
#     else:
#         d[i] = i[::-1]
# print(d)
# print({i: i if len(i) % 2 == 0 else i[::-1] for i in a})
#

# d = {'a': 'apple', 'b': 1234, 'c': 432}
# print({i: j if isinstance(j, str) else int(str(j)[::-1]) for i, j in d.items()})
#

# a = [1, 2, 3, 4, 5]
# b = [3, 5, 7]
# print([i+j for i, j in zip(a, b)])
#
# res = []
# for n in a:
#     fac = 1
#     for i in range(1, n+1):
#         fac *= i
#     res.append(fac)
# print(res)
#
# from math import factorial
# print([factorial(i) for i in a])
