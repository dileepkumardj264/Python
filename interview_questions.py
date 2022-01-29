import csv
import itertools
import random
from collections import defaultdict, Counter
import re
from datetime import datetime, date
from functools import reduce
#
#
# def sam(s):
#     for index, ele in enumerate(s):
#         if ele in 'AEIOU' and index % 2==0:
#             print(ele, end=' ')
#     print()
#
#
# sam('HELLOHOWAREYOU')
#
#
# def even(s):
#     for i in s:
#         if i.isdigit() and int(i) % 2 == 0:
#             print(i, end=' ')
#     print()
#
#
# even('13435464788')
#
# a= [1, 2, 3, 'hai', True, 3+2j, (1, 2)]
#
# d = {}
# for i in a:
#     if isinstance(i, (int, float, complex, bool)):
#         d[i] = 'success'
#     else:
#         d[i] = 'Failure'
# print(d)
#
# s = 'hai@#$%^'
# count = 0
# for i in s:
#     if not i.isalnum():
#         count += 1
# print(count)
#
# s = 'haihello'
# import re
# print(re.sub('[aeiou]', '*', s))
# out = ''
# for i in s:
#     if i in 'aeiou':
#         out += '*'
#     else:
#         out += i
# print(out)
# res = ''
# for i in s:
#     if i in 'aeoiu':
#        res += str(ord(i))
#     else:
#         res += i
# print(res)
#
#
# def add(a, b):
#     return a + b
#
#
# def sub(a, b):
#     return a - b
#
#
# def mul(a, b):
#     return a * b
#
#
# def div(a, b):
#     return a//b
#
# s = 'hello2344hhiwff'
#
# for index, ele in enumerate(s):
#     if ele.isalpha() or (ele.isnumeric() and index % 2 == 0):
#         print(ele, end=' ')
# print()
#
# l = [1, 2, 3, 4]
# l.insert(4, 20)
# print(l)
# res = []
# for i in range(0, len(l)):
#     if i == 4:
#         res += [10]
#     res += [l[i]]
# print(res)
#
#
#
# a = 20
# def sam():
#     global a
#     a += 100
#     print(a)
#
#
# sam()
# print(a)
# a += 20
# print(a)
#
# def sam():
#     m = 20
#     def inner():
#         nonlocal m
#         m += 20
#         print(m)
#         m += 10
#     inner()
#     print(m)
#     m+=10
# sam()
#
# def sam(*arg):
#     for i in arg:
#         if i % 2 == 0:
#             print(i, end=' ')
#     print()
#
# sam(1, 2, 3, 4, 5)
#
#
# def sam(n):
#     if n ==1:
#         return 1
#     return n + sam(n-1)
#
#
# print(sam(5))
#
#
# def fac(n):
#     if n == 1:
#         return 1
#     return n * fac(n-1)
#
#
# print(fac(5))
#
#
# def sam(s, i=0, res=''):
#     if i >= len(s):
#         return res
#     res = s[i] + res
#     return sam(s, i+1, res)
#
#
# print(sam('hello'))
#
#
# def fib(i, j, count=10):
#     if count<= 0:
#         return
#     print(i)
#     temp = i+j
#
#     return fib(i=j, j=temp, count=count-1)
#
#
# fib(0, 1)
#
# sum = lambda a, b, c, d, e: a+b+c+d+e
# print(sum(1, 2, 3, 4, 5))
#
#
# sam = lambda a: isinstance(a, complex)
# print(sam(3+2j))
#
# sa = lambda a: a**3
# print(sa(3))
#
# out = lambda a: isinstance(a, (str, list, tuple, set, dict))
# print(out('hello'))
# print(out([2,3,4]))
# print(out(2))
#
# res = lambda a: not a.isalnum()
# print(res('&'))
# print(res('a'))
#
#
# print(list(map(lambda a, b: a**b, [2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5])))
#
# out = lambda a:a[len(a)//2].isalpha()
# print(out('hello'))
#
# res = lambda a, b: a**2 + b**2 + 2*a*b
# print(res(2,3))
#
# even = lambda n: n%2 == 0
# print(even(4))
#
# palindrome = lambda s: 'palindrome' if s==s[::-1] else 'not a palindrome'
# print(palindrome('mam'))
#
# print(list(map(lambda a: ord(a)**2, ('hello'))))
#
# print(list(filter(lambda s: s==s[::-1], ['mam', 'dad', 'mom', 'hello'])))
#
# sq = list(map(lambda n: n**2, [2, 3, 4, 5]))
# cube = list(map(lambda n: n**3, [2, 3, 4, 5]))
# print([*sq, *cube])
#
# print(list(map(lambda i: i[0]**i[1], enumerate([1, 2, 3, 4]))))
#
# print(list(map(lambda n:abs(n), [1,-2, -3])))
#
# print(list(filter(lambda n : n%2, [1, 2, 3, 4, 5])))
#
# print(list(filter(lambda s: len(s)%2, ['hai', 'tell', 'your', 'name'])))
#
# print(list(filter(lambda s: s[0] in 'aeiouAEIOU', ['ear', 'apple', 'icecream', 'hello'])))
#
# print(list(filter(lambda n: n<0, [1, 2, -3, -2, -4])))
#
# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     else:
#         return True
#
#
# print(list(filter(prime, range(2,50))))
#
#
# def armstrong(n):
#     sum = 0
#     for i in str(n):
#         sum += int(i) ** len(str(n))
#     if n == sum:
#         return True
#
#
# print(list(filter(armstrong, range(1,5000))))
#
# a = [1, 2, 3, 4, 5]
#
# s = reduce(lambda a,b: a**b, a)
# print(s)
#
# def sam(s, ch):
#     for i in s:
#         if i == ch:
#             return s.index(ch)
#
#
# print(sam('hello', 'l'))
#
# def sam(s, n):
#     return s[n::2]
#
#
# print(sam('TRACXN', 0))
#
#
# def sam(n):
#     return int(str(n)[-1])
#
#
# print(sam(23456))
#
# s = 'hai hello how program are you'
# l = s.split()
# # l.sort(key=len)
# # print(l[-1])
#
# word = ''
# maximum = 0
# for i in l:
#     if len(i)> maximum:
#         maximum = len(i)
#         word = i
# print(word)
#
# d = {word:len(word) for word in s.split()}
# print(min(d, key=len))
# print(sorted(d, key=len)[0])
# names = ['dillep', 'divya', 'darvin', 'daliya', 'dimpana']
# print(sorted(names))
# print(sorted(names, key=len))
# print(sorted(names, key=lambda s:s[-1]))
# print(sorted(names, key=lambda s: s[len(s)//2]))
#
# s = 'python is a programming langauge and programming is fun'
# d = {word:len(word) for word in s.split()}
# *rest, x = sorted(d.items(), key=lambda item:item[-1])
# print(x)
#
# students = [{'name':'john', 'age':32}, {'name':'dileep', 'age':34}]
# print(sorted(students, key=lambda item:item['name']))

sample_txt = r'C:\Users\Dileep\pythonProject24\newfiles\sample.txt'
#
# with open(sample_txt, 'r') as f:
#     for line in f:
#         if line.strip():
#             for item in line.split():
#                 print(item, end=' ')
#             print()
#
# with open(sample_txt) as f:
#     count = 0
#     for line in f:
#         if line.strip():
#             res = re.findall('hello', line)
#             count += len(res)
#     print(count)
#
# with open(sample_txt) as f:
#     count = 0
#     for line in f:
#         if line.strip():
#             a = line.split()
#             count += len(a)
#     print(count)
#
# with open(sample_txt) as f:
#     count = 0
#     for line in f:
#         if line.strip():
#             count += 1
#     print(count)
#
# with open(sample_txt) as f:
#     for lno, line in enumerate(f, start=1):
#         if line.strip():
#             print(lno, line)
#
# with open(sample_txt) as f:
#     a = list(f)
#     for line in a[::-1]:
#         if line.strip():
#             print(line)
#
# with open(sample_txt) as f:
#     print(f.read(10))
#
# with open(sample_txt) as f:
#     for line in f:
#         print(len(line))
#
# access_log = r'C:\Users\Dileep\pythonProject24\newfiles\access-log.txt'
#
# with open(access_log) as f:
#     for line in f:
#         a = line.split()
#         print(a[-1])
#
# with open(access_log) as f:
#     l =[]
#     for line in f:
#         a = line.split()
#         if a[0] not in l:
#             l.append(a[0])
#     print(l)
#
# with open(access_log) as f:
#     d = defaultdict(int)
#     for line in f:
#         a = line.split()
#         d[a[0]] += 1
#     print(d)
#     *rest, y = sorted(d.items(), key=lambda item: item[-1])
#     print(y)
#
# from collections import defaultdict
#
# sample_log = r'C:\Users\Dileep\pythonProject24\newfiles\sample.log'
#
# with open(sample_log) as f:
#     for line in f:
#         if line.strip():
#             a = line.split()
#             print(a[2])
#
# with open(sample_log) as f:
#     d = defaultdict(int)
#     for line in f:
#         if line.strip():
#             a = line.split()
#             d[a[2]] += 1
#     print(d)
#     x, *rest, y = sorted(d.items(), key=lambda item:item[-1])
#     print(x, y)
#
# with open(sample_txt) as f:
#     d = Counter()
#     for line in f:
#         d += Counter(line)
#     print(d[' '])
#
# sample_csv = r'C:\Users\Dileep\pythonProject24\newfiles\sample.csv'
# with open(sample_csv) as f:
#     rows = csv.reader(f)
#     for row in rows:
#         print(row)
#
# employee_csv = r'C:\Users\Dileep\pythonProject24\newfiles\employees.csv'
# with open(employee_csv) as f:
#     rows = csv.DictReader(f)
#     for row in rows:
#         print(row)

# with open(sample_csv, 'a+') as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow([23, 45, 56, 67])

# d = defaultdict(int)
# def outer(func):
#     def wrapper(*args, **kwargs):
#         fname = func.__name__
#         d[fname] += 1
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @outer
# def add(a, b):
#     return a+b
#
# @outer
# def sub(a,b):
#     return a-b
#
#
# print(add(2, 3))
# print(add(2, 3))
# print(add(2, 3))
# print(sub(5,3))
# print(sub(5,3))
# print(d)
#
#
# def pouter(n):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 yield (func(*args, *kwargs))
#         return wrapper
#     return outer
#
#
# @pouter(3)
# def add(a, b):
#     return a+b
#
#
# print(list(add(3,4)))
#
# l = [1, 2,3 ,4, 0]
# print(all(l))
#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         for i in args:
#             if not(isinstance(i,int)):
#                 return 'invalid input'
#         else:
#             return func(*args, **kwargs)
#     return wrapper
#
#
# @outer
# def rev(a, b, c=0):
#     return a + b + c
#
#
# print(rev(2, 4, 6))
#
#
# with open(sample_txt) as f:
#     for lno, line in enumerate(f, start=1):
#         if lno == 2:
#             print(line)
#
# l = ['apple', 'yahoo', 10, 'gmail',12,  'google']
# for item in l:
#     try:
#         print(item[0])
#     except Exception as msg:
#         print(msg)
#

#
# class sample:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.iter_ = iter(self.iterable)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             return next(self.iter_)
#         except StopIteration:
#             print('no elements')
#
#
# s = sample('hello')
# print(next(s))
# print(next(s))
#
#
# class Numbers:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.end:
#             self.start += 1
#             return self.start
#         else:
#             raise StopIteration
#
# s = Numbers(0, 10)
# for i in s:
#     print(i)
#
# class Number:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
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
# n = Number(11, 1)
# for i in n:
#     print(i)
#
# class Reversed:
#
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.index = len(self.iterable)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index > 0:
#             self.index -= 1
#             return self.iterable[self.index]
#         else:
#             raise StopIteration
#
# m = Reversed(['hia', 'hello', 'how', 'are', 'you'])
# for i in m:
#     print(i)
# from time import sleep
#
# l = ['on', 'off', 'hello']
# res = itertools.cycle(l)
# for i in range(5):
#     print(next(res))

#
# res = itertools.repeat(l, 6)
# for i in range(5):
#     print(next(res))
#
# res = itertools.count(2)
# for i in res:
#     print(i)
#     if i ==10:
#         break
#
# res = itertools.permutations(l)
# for i in res:
#     print(i)
#
# res = itertools.combinations(l,2)
# for i in res:
#     print(i)
#
# res = itertools.combinations(l,3)
# for i in res:
#     print(i)
#
# with open(sample_txt) as f:
#     res = itertools.islice(f, 2, 5)
#     for line in res:
#         print(line)


# print(random.randrange(5))
# print(random.randint(1, 5))
# print(random.random())
# print(random.uniform(1,5))
# print(random.choice('hello'))
# print(random.sample('hello', 3))

td = datetime(2021,2,20)
print(td.year)
print(td.day, td.weekday(), td.month)
print(date.today())