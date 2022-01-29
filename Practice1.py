# # WAP to find the length of an iterable without using inbuilt function
# s = 'hello'
# length = 0
# for _ in s:
#     length += 1
# print(length)
#
# # WAP to reverse a string without using any inbuilt method
# res = ''
# for i in s:
#     res = i + res
# print(res)
#
# #WAP to replace one string with another
# s = 'hello world'
# a = s.split()
# l = []
# for i in a:
#     if i == 'world':
#         l.append('universe')
#     else:
#         l.append(i)
# m = ' '.join(l)
# print(m)
#
# a = s.replace('world', 'universe')
# print(a)
#
# # WAP to convert a list into a string & vice versa
# s = 'hello'
# a = list(s)
# print(a)
# print(''.join(a))
#
# # convert the string to comma separated string
# s = 'hello welcome to python'
# print(','.join(s))
# a = s.split()
# print(",".join(a))
# print(s.replace(' ', ','))
# print(*s, sep=',')
# print(*a, sep=',')
#
#
# #WAP to print alternate charcter in a string
#
# for i in range(len(s)):
#     if i % 2 == 0:
#         print(s[i])
# print(s[::2])

# WAP to print ASCII value of a charcter oresent in a string
# s = 'hello world'
# for i in s:
#     print(ord(i))
# print({i: ord(i) for i in s})

# WAP to covert upper to lower and vice versa
#
# s = 'Hai HEllo'
# res = ''
# for i in s:
#     if 'A' <= i <= 'Z':
#         res += chr(ord(i) + 32)
#     elif 'a' <= i <= 'z':
#         res += chr(ord(i) - 32)
#     else:
#         res += i
# print(res)
#
# out = ''
# for i in s:
#     if i.isupper():
#         out += i.lower()
#     elif i.islower():
#         out += i.upper()
#     else:
#         out += i
# print(out)

# print(s.swapcase())

#WAP to swap to numbers without using third variable
# a = 10
# b = 20
# a, b = b, a
# print(a, b)
#
#
# #WAP to merge two list and two dict
# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]
# m = [*l1, *l2]
# print(m)
# t = (5, 6, 7, 8)
# print([*l1, *t])
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# print({**d1, **d2})

#wap to read random line from a file
import re

path = r'C:\Users\Dileep\pythonProject24\newfiles\sample.txt'
import itertools
# def line(n):
#     with open(path) as f:
#         res = itertools.islice(f, n-1, n)
#         print(list(res))
#
# line(6)

# with open(path) as f:
#     l = 4
#     for lno, line in enumerate(f, start = 1):
#         if lno == l:
#             print(line)

#WAP to read random lines from a file
# def lines(n1, n2):
#     with open(path) as f:
#         res = itertools.islice(f, n1-1, n2)
#         print(list(res))
#
#
# lines(3, 4)

# without using inbuilt function
# start = 3
# end = 6
# with open(path) as f:
#     count = 0
#     for line in f:
#         count += 1
#         if start <= count <= end:
#             print(line)

# with open(path) as f:
#     for lno, line in enumerate(f, start=1):
#         if start <= lno <= end:
#             print(line)

# WAP to print last line in the file
# def lastline(n):
#     with open(path) as f:
#         count = 0
#         for line in f:
#             count += 1
#         print(count)
#         f.seek(0)
#         lineno = 0
#         for line in f:
#             lineno += 1
#             if count - n < lineno <= count:
#                 print(line)
#
#
# lastline(3)


# using islice
# def lastline(n):
#     with open(path) as f:
#         count = 0
#         for line in f:
#             count += 1
#         print(count)
#         f.seek(0)
#         res = itertools.islice(f,count-n, count)
#         print(list(res))
#
#
# lastline(3)


# using deque
# from collections import deque
#
# with open(path) as f:
#     res = deque(f,3)
#     print(list(res))

# WAP to check the given string is palindrome or not
# s = 'mam'
# if s == s[::-1]:
#     print('palindrome')
# else:
#     print('non palindrome')

# wap to check for the chr in a given string and return its corresponding index
# s = 'hello'
# for index, chr in enumerate(s):
#     if chr == 'l':
#         print(chr, index)
#
# for i in range(len(s)):
#     if s[i] == 'l':
#         print(s[i], i)


# wap to get the dic
# s = 'hello world welcome to python programming hi there'
# l = s.split()
# from collections import defaultdict
# d = defaultdict(list)
# for i in l:
#     d[i[0]] += [i]
# print(d)
#
# d1 = {}
# for i in l:
#     if i[0] not in d1:
#         d1[i[0]] = [i]
#     else:
#         d1[i[0]] += [i]
# print(d1)

# WAP to replace all the chacters with - if the characters occurs morethan once in a string
# s = 'hellohai'
# res = ''
# for i in s:
#     if s.count(i) > 1:
#         res += '-'
#     else:
#         res += i
# print(res)

#WAP a decorator that returns only positive values of substarction
#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper
#
#
# @outer
# def sub(a, b):
#     return a - b
#
#
# print(sub(3,6))

# How to get the count of number of instances of a class that is being created

# class Bank:
#     count = 0
#     def __init__(self, name):
#         Bank.count += 1
#
# s = Bank('ram')
# f = Bank('re')
# m = Bank('hvy')
# print(Bank.count)

# Write a function which takes a list of strings and integers.
# If the item is a string it should print as is and if the item is integer of float it should reverse it.

# def sam(l):
#     for i in l:
#         if isinstance(i, str):
#             print(i)
#         elif isinstance(i,(int, float)):
#             print(float(str(i)[::-1]))
#
#
# sam(['hai', 'hello', 23.4, 456])


# Write a class named Simple and it should have iteration capability

# class Simple:
#
#     def __init__(self, name):
#         self.names = name
#
#     def __iter__(self):
#         return iter(self.names)
#
#
#
# s = Simple(['ra', 'AA', 'BB', 'CC'])
# print(s)
# for i in s:
#     print(i)
#

# Write a Custom class which can access the values of dictionaries using d['a'] and d.a

# class Mydict:
#
#     def __init__(self, d):
#         self.dict = d
#
#     def __getitem__(self, item):
#         return self.dict[item]
#
#     def __getattr__(self, word):
#         return self.dict[word]
#
#
# d = Mydict({'a': 1, "b": 2})
# print(d.a)
# print(d['b'])


# Write a python program to get the below output**

# s = "Hi How are you"
# # o/p should be "iH woH era uoy"
# a = s.split()
# l = []
# for i in a:
#     l.append(i[::-1])
# print(' '.join(l))
#
#
# # o/p 'uoy era woH iH'
# print(s[::-1])
#
# # Write a lambda function to add two numbers (a, b)
#
# res = lambda a, b : a+b
# print(res(2, 3))
#
#
# # What is the output of the following**
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# print([a, b])
# print((a, b))

# How to remove duplicates from the list without using inbuilt functions

# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# print(list(set(items)))
#
# l = []
# for i in items:
#     if i not in l:
#         l.append(i)
# print(l)

# Find the longest word in the sentence

# s = "Hello world. Welcome to Python"
# a = s.split()
# res = list(sorted(a, key=len))
# print(res[-1])

# length = 0
# max_word = ''
#
# for i in a:
#     if len(i) > length:
#         length = len(i)
#         max_word = i
# print(max_word)

# l = [1, 6, 33, 4, 9]
# for i in range(len(l)-1):
#     for i in range(len(l)-1):
#         if l[i] > l[i+1]:
#             l[i], l[i+1] = l[i+1], l[i]
# print(l)

# write a program to reverse the values in the dictionary if the value is of type String
# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

# write a program to get 1234
# t = ('1', '2', '3', '4')
# print(''.join(t))

# How to get the elements that are in list b but not in list a**
# a = [1, 2, 3]
# b = [1, 2, 3, 4]
# for i in b:
#     if i not in a:
#         print(i)

# print(set(b) - set(a))

# A function takes variable number of positional arguments as input.
# How to check if the arguments that are passed are more than 5

# def sam(*args):
#     if len(args) > 5:
#         print('arguments are more than 5')
#     else:
#         print('arguments are less than 5')
#
#
# sam(1, 2, 3, 4, 5, 6)


# Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.

# d = {}
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             a = line.split(':')
#             if a[0] not in d:
#                 d[a[0]] = 1
#             else:
#                 d[a[0]] += 1
# print(d)
#
# # Using default dict
#
# from collections import defaultdict
# d = defaultdict(int)
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             a = line.split(':')
#             d[a[0]] += 1
# print(d)

# def sam(s, n):
#     for i, j in enumerate(s):
#         if i % 2 != n:
#             print(j, end='')
#     print()
#
#
# sam('TRACXN', 1)
#
#
# def sam(s, n):
#     if n == 0:
#         return s[1::2]
#     elif n == 1:
#         return s[::2]
#
#
# print(sam('TRACXN', 0))


# Sum all the numbers in the below string
# s = "Sony12India567Pvt2ltd"
# sum = 0
# for i in s:
#     if i.isdigit():
#         sum += int(i)
# print(sum)
#
#
# import re
# m = re.findall('[0-9]', s)
# total = 0
# for i in m:
#     total += int(i)
# print(total)

# Write a program to sum all the numbers in below string.**
# s = "Sony12India567Pvt2ltd" # eg.12+567+2

# out = re.findall('\d+', s)
# total = 0
# for i in out:
#     total += int(i)
# print(total)


# Print all the numbers in the below list**
# a = ['abc', '123', 'hello', '23']
#
# for i in a:
#     if i.isdigit():
#         print(i)

# Program to print the number of occurrences of characters in a String without using inbuilt functions

# string = 'hello'
# from collections import Counter
#
# d = Counter(string)
# print(d)
#
# def count_(string, chr, count = 0):
#     for i in string:
#         if i == chr:
#             count += 1
#
#     return count
#
#
# print(count_('Malayalam', 'a'))

# Program to print only the repeated characters and count of the same

# string = 'hello'
#
# for i in string:
#     if string.count(i) > 1:
#         print(i, string.count(i))

# d = defaultdict(int)
# for i in string:
#     if string.count(i) > 1:
#         d[i] +=1
# print(d)


# # Write a program to get alternate characters of a string in list format
# s = 'hello world'
# print(list(s[::2]))
#
# m = []
# for index, value in enumerate(s):
#     if index % 2 == 0:
#         m.append(value)
# print(m)


# Write a program to get square of list of number's using lambda function

# l = [1, 2, 3, 4, 5]
# print((list(map(lambda a: a**2, l))))

# Write a function that accepts two strings and returns True if the two strings are anagrams of each other

# def angrams(string1, string2):
#     if sorted(string1) == sorted(string2):
#         print('the two strings are anagrams')
#     else:
#         print('the two strings are not anagrams')
#
#
# angrams('fare', 'fear')

# Write a program to iterate through list and build a new list,
# only if the items of the list has even number of characters

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
#
# print([i for i in names if len(i) % 2 == 0])

# Write a program to iterate through list and build a new dictionary,
# only if the items of the list has even number of characters

# print({i: len(i) for i in names if len(i) % 2 == 0})


# Write a program which squares the numbers in a list using map object**
# a = [1, 2, 3, 4, 5]
# print(list(map(lambda i: i*i, a)))

# Count number of lines in a file without loading the file to the memory

# Write a program to replace value present in nested dictionary.**
# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
#
# d['b']['n'] = 'net'
# print(d)
# # Replace "nose" with "net"
#
#
# def change_value(iterable, old, new):
#
#     for key, value in d.items():
#         if isinstance(value, dict):
#             for k, v in value.items():
#                 if v == old:
#                     value[k] = new
#         else:
#             if value == old:
#                 d[key] = new
#     print(d)
#
#
# change_value(d, 'nose', 'net')


# Write a program to count the number of white spaces in a file

# with open(path) as f:
#     count = 0
#     for line in f:
#         if line.strip():
#             for i in line:
#                 if i == ' ':
#                     count += 1
#     print(count)


# words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
# from collections import defaultdict
#
# d = defaultdict(list)
# for i in words:
#     s = ''.join(sorted(i))
#     d[s] += [i]
# print(d)


# property Decorator

# class Employee:
#
#     def __init__(self, sal):
#         self.__sal = sal
#
#     @property
#     def salary(self):
#         return self.__sal
#
#     @salary.setter
#     def salary(self, newvalue):
#         self.__sal = newvalue
#
#     @salary.deleter
#     def salary(self):
#         del self.__sal
#
#
# e = Employee(20000)
# print(e.salary)
# e.salary = 10000
# print(e.salary)
# del e.salary

# Write a list comprehension to get a list of even numbers from 1-50

# print([i for i in range(1, 51) if i % 2 == 0])

# Find the longest non-repeated substring in the below string
#
# s = "This is a Programming language and Programming is fun"
# d = {i: len(i) for i in s.split() if s.split().count(i) == 1}
# a = sorted(d.items(), key=lambda item: item[-1])
# print(a[-1])

# a = s.split()
# max_word =''
# for i in a:
#     if a.count(i) == 1:
#         if len(i) > len(max_word):
#             max_word = i
# print(max_word)
# print(a)
# for i in range(len(a)):
#     for j in range(len(a)):
#         if len(a[i]) < len(a[j]):
#             a[i], a[j] = a[j], a[i]
# print(a)


# Write a program to find the duplicate elements in the list without using inbuilt functions

# non_dup = []
# dup = []
# for i in l:
#     if i not in non_dup:
#         non_dup.append(i)
#     else:
#         dup.append(i)
#
# print(dup, non_dup)

# Write a program to count the number occurrences of each item in the list without using any inbuilt functions**
# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# from collections import Counter
# d = Counter(names)
# print(d)

# Write a function to check if the number is Prime

# def Prime_(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return 'non prime'
#     return 'prime'
#
#
# print(Prime_(5))
#
#
# def Prime_(n):
#     for i in range(n):
#         if i > 1:
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             print(i)
#
#
# print(Prime_(5))

# How to create a tuple of numbers from 0 to 10 using range function

# print(tuple(range(1, 10)))

# Write a program to find the largest number in the list without using any inbuilt functions


# Write a program to find most common words in a given list.**
# words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
# 'eyes', 'look', 'into','my', 'eyes', "you're", 'under']
# #
# from collections import Counter
# res = (Counter(words))
# print(res.most_common(1))
# print((sorted(res.items(), key=lambda item: item[-1]))[-1])

# Make a function named tail that takes a sequence (like a list, string, or tuple) and
# a number n and returns the last n elements from the given sequence, as a list.

# def tail(iterable,n):
#     return list(iterable[-n:])
#
#
# print(tail('hello world', 3))
#
#
# from collections import deque
# def tail(iterable, n):
#     return list(deque(iterable, n))
#
#
# print(tail('hello world', 2))
#
#

# def sam(*args):
#     l =[]
#     for i in args:
#         if isinstance(i, int):
#             l.append(int(str(i)[-1]))
#         elif isinstance(i, (str, list, tuple)):
#             l.append(i[-1])
#     print(l)
#
#
# sam('hai', [1, 2, 3], (4, 5, 6), 345)


# Write function named is_perfect_square that accepts a number and
# returns True if it's a perfect square and False if it's not

# def perfect_square(n):
#
#     if round(n**0.5) * round(n**0.5) == n:
#         return True
#     else:
#         return False
#
#
# print(perfect_square(4))


# Write a program to get all the duplicate items and the number of times the item is repeated in the list.**
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
#
# d = {}
# for i in names:
#     if names.count(i) > 1:
#         d[i] = names.count(i)
#
# print(d)
#
# dd = {i: names.count(i) for i in set(names) if names.count(i)>1}
# print(dd)

# Write a program to count the number of occurrences of each word in a file


from collections import defaultdict, Counter
# with open(path) as f:
#     d = defaultdict(int)
#     for line in f:
#         if line.strip():
#             a = line.split()
#             for i in a:
#                 d[i] += 1
#     print(d)
#
# with open(path) as f:
#     dd = Counter()
#     for line in f:
#         if line.strip():
#             a = line.split()
#             dd += Counter(a)
#     print(dd)

# Write a program to count the number of occurrences of vowels in a file

# with open(path) as f:
#     Count = 0
#     for line in f:
#         for i in line:
#             if i in 'aeiouAEIOU':
#                 Count += 1
#     print(Count)

# Write a program to print all numeric values in a list**

# items = ['apple', 1.2, 'google', '12.6', 26, '100']
#
# for i in items:
#     if isinstance(i, (int, float)):
#         print(i)

# for i in range(1, 5):
#     print('* ' * i)
#
# for i in range(5, 0, -1):
#     print('* ' * i)

# for i in range(1, 6):
#     print(f'{"* " * i:>12}')
#
# for i in range(1, 6):
#     print(f'{"* " * i:^12}')
#
# for i in range(6, 0, -1):
#     print("* " * i)
#
# for i in range(6, 0 ,-1):
#     print(f'{"* " * i:>12}')
#
# for i in range(6, 0, -1):
#     print(f'{"* " * i:^12}')


# pat = ''
# for i in range(1, 6):
#     pat += str(i) + ' '
#     print(pat)

# pat = ''
# for i in range(1, 6):
#     pat += str(i) + ' '
#     print(f'{pat:^12}')

# Write a program count the occurrence of a particular word in the file

# with open(path) as f:
#     count = 0
#     for line in f:
#         a = line.split()
#         for word in a:
#             if word == 'hello':
#                 count += 1
#     print(count)

# Write a program to map a product to a company and build a dictionary with company and list of products pair**
# all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows',
#                 'iOS', 'Google Drive', 'One Drive']
#
# # Pre-defined products for different companies
# apple_products = {'iPhone', 'Mac', 'iWatch'}
# google_products = {'Gmail', 'Maps', 'Google Drive'}
# msft_products = {'Windows', 'One Drive'}
#
# d = defaultdict(list)
#
# for i in all_products:
#     if i in apple_products:
#         d['apple_products'] += [i]
#     elif i in google_products:
#         d['google_products'] += [i]
#     elif i in msft_products:
#         d['msft_products'] += [i]
# print(d)

# Write a program to rotate items of the list**
# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]

# l1 = []
# for i in names:
#     l1.append(i[::-1])
# print(l1)


# n = 3
# for i in range(n):
#     f = names.pop()
#     names.insert(0, f)
# print(names)

# print(names[-n:] + names[:n])

from collections import deque
#
# def sam(l1, n):
#     d = deque(l1)
#     d.rotate(n)
#     return list(d)
#
#
# print(sam(s, 2))

# Write a program to rotate characters in a string
# n = 2
# s = 'hello'
# m = list(s)
# for i in range(n):
#     f = m.pop()
#     m.insert(0, f)
# print(''.join(m))


# Write a program to count the number of white spaces in a given string
#
# s = 'hai hello how are you'
# count = 0
# for i in s:
#     if i == ' ':
#         count += 1
# print(count)

# Write a program to print only non-repeated characters in a string

# s = 'helloworld'
# for i in s:
#      if s.count(i) == 1:
#          print(i)

# s = [1, 2, 3, 4]
# n = 3
# d = deque(s)
# for _ in range(n):
#     d.appendleft(d.pop())
# print(list(d))

# Write a program to print all the consonants in a given string

# s = 'hello world'
# for i in s:
#     if i not in 'aeiouAEIOU':
#         print(i)

# Write a program to count the number of commented lines in a text file

# with open(path) as f:
#     for line in f:
#         if line[0] == '#':
#             print(line)

# Write a program to check if the year is leap year or not
# year = 2012
# print('its a leap year' if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 'it is not a leap year')
# #
# import calendar
# print(calendar.isleap(year))

# Write a program to count no of capital letters in a string

# s = 'DNPIOdwefu'
# count = 0
# for i in s:
#     if i.isupper():
#         count += 1
# print(count)

# pat = ''
# for i in range(2, 6):
#     print('*')
#     print("* " * i)

# Write a program to get the below output
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in range(0, len(a), 2):
#     print(a[i:i+2])



# # Write a program to check if the elements in the second list is series of continuation of the items in the first list**
#
# a = [2, 4, 6, 8]
# b = [10, 12, 14, 16]
# c = [*a, *b]
# dif = c[1] - c[0]
# for i in range(len(c)-1):
#     if c[i+1] - c[i] != dif:
#         print('its not a continuous')
#         break
# else:
#     print('its a continuous')

# Write a program to find the first repeating character in a string

# s = 'hellooo'
# res = ''
# for i in s:
#     if i not in res:
#         res += i
#     else:
#         print(i)
#         break

# Write a program to find the index of nth occurrence of a sub-string in a string**

# s = "hello world welcome to python hello hi how are you hello there"
# # print(s.rindex('hello'))
# n = 3
# sv = 0
# count = 0
# for i in s:
#     m = s.index('hello',sv)
#     count += 1
#     sv += m + 1
#     if count == n:
#         print(m)
#         break
#
# import re
# def sam(s, pattern, n):
#
#     a = re.finditer(pattern, s)
#     count = 0
#     for i in a:
#         count += 1
#         if count == n:
#             print(i.start(), i.end())
#
#
# sam(s, 'hello', 2)


# Write a program to print prime numbers from 1 to 50

# for n in range(1, 50):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             print(n)

# Write a program to sort a list which has mix of both odd and even numbers,
# the sorted list should have odd numbers first and then even numbers in sorted order
#
# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
#
# odd = [i for i in a if not i % 2 == 0]
# even = [i for i in a if i % 2 == 0]
# odd.sort()
# even.sort()
# print([*odd, *even])

# Write a program to count the number of occurrences of non-special characters in a given string

# s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
# d = defaultdict(int)
# res = re.findall('\w', s)
# for i in res:
#     d[i] += 1
# print(d)

# dd = Counter()
# for i in s:
#     if i.isalnum():
#         dd += Counter(i)
# print(dd.most_common(2))


# Grouping Flowers and Animals in the below list
# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
# d = defaultdict(list)
# for i in items:
#     item, group = i.split("-")
#     d[group] += [item]
# print(d)

# Grouping files with same extensions
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
# d = defaultdict(list)
# for i in files:
#     name, extension = i.split(".")
#     d[extension] += [name]
# print(d)


# Filter only those characters except digits**
# s = '@hello12world34welcome!123'
#
# print(''.join(list(filter(lambda i: not(i.isdigit()), s))))
#
# print(''.join(re.findall('\D', s)))
#
# # Count number of words in a sentence. ignore special characters.**
# sentence = "Hi there! How are you:) How are you doing today!"
# count = 1
# for i in sentence:
#     if i == ' ':
#         count += 1
# print(count)
#
# print(re.findall('\w+', sentence))

# Grouping even and odd numbers**
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# o/p should be {1: [1, 3, 5, 7, 9], 0: [2, 4, 6, 8, 10]}

# d = defaultdict(list)
# for i in numbers:
#     if i % 2 == 0:
#         d[0] += [i]
#     else:
#         d[1] += [i]
# print(d)

# Find all max numbers from the below list**
# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# list_ = []
# n = max(numbers)
# for i in numbers:
#     if i == n:
#         list_.append(i)
# print(list_)

# Find all max length words from the below sentence**
# sentence = "hello world hi apple you yahoo to you"
# max_word = max(sentence.split(), key=len)
# print([word for word in sentence.split() if len(word) == len(max_word)])

# Find the range from the following string**
# sentence = '0-0, 4-8, 20-20, 43-45'
# # Output Should be [0, 4, 5, 6, 7, 8, 20, 43, 44, 45, 46]
# words = sentence.split(',')
# op = []
# for word in words:
#     start, end = word.split('-')
#     for i in range(int(start), int(end)+1):
#         op.append(i)
# print(op)

# Write a function which returns the sum of lengths of all the iterables**
# def total_length(*args):
#     count = 0
#     for i in args:
#         count += len(i)
#     print(count)
#
#
# total_length([1, 2, 3], (4, 5), ['apple', 'google', 'yahoo', 'gmail', 'flipkart'], {1, 2, 3}, {'a': 1, 'b': 2})

# Replace whitespaces with newline character in the below string**
# sentence = "Hello world welcome to python"
# print(sentence.replace(' ', '\n'))
# print(re.sub('\s', '\n', sentence))


# Replace all vowels with "*"**
# print(re.sub('[aeiou]', '*', sentence))


