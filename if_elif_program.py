# a = int(input("enter the value1:"))
# b = int(input("enter the value2:"))
# c = int(input("enter the value3:"))
# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")
# if a>b: print("a is greater")
# print("a is greater") if a>b else print("b is greater")
# a=16
# b=13
# c=20
# if a>b:
#     if a>c:
#         print("a is greater")
#     else:
#         print("c is greater")
# elif b>c:
#     print("b is greater")
# else:
#     print("c is greater")

# s = input("enter the character:")
# print(chr(ord(s)-32)) if "a" <= s <= 'z' else print(chr(ord(s)+32))


# s = input("enter the character:")
# # d = {}
# if s in "aeiouAEIOU":
#     d = dict([(s, ord(s))])
#     print(d)
# else:
#     print("not vowel")

# s="a"
# print(dict([(s,ord(s))]) if s in "aeiouAEIOU" else "not a vowel")

# l = [1,2]
# print("list is not empty" if l else "list is empty")

# s="a"
# print("ch is vowel" if s in "aeiouAEIOU" else "ch is not a vowel")

# d = {'a': 1, 'b': 2}
# key = input("enter the key:")
# if key in d:
#     d[key] += 1
# else:
#     d[key] = 1
# print(d)

# s = 'hai'
# if type(s) == str:
#     print("its a string")
# else:
#     print("its not a string")
#

# s = 10
# print("its a string" if isinstance(s,str) else "its a not string")


# d = {'a': "apple", "f": "facebook", "c": 10, "d": 1.25}
# for i in d:
#     if isinstance(d[i],str):
#         d[i] = d[i][::-1]
# print(d)

# d = {}
# n = int(input("enter the number of value:"))
# for i in range(n):
#     key = input("enter the key:")
#     value = input('enter the value:')
#     d[key] = value
# print(d)
# for i in d:
#     if isinstance(d[i], str):
#         d[i] = d[i][::-1]
# print(d)

# d = {'a': "apple", "f": "facebook", "c": 10, "d": 1.25}
# if isinstance(d['a'], str): d['a'] = d['a'][::-1]
# if isinstance(d['f'], str): d['f'] = d['f'][::-1]
# if isinstance(d['c'], str): d['c'] = d['c'][::-1]
# if isinstance(d['d'], str): d['d'] = d['d'][::-1]
# print(d)

# key = input("enter the key:")
# if isinstance(d[key], str):
#     d[key] = d[key][::-1]
# print(d)



# n = int(input("enter the number:"))
# print(f" {n} is even number" if n % 2 == 0 else f" {n} is odd number")

# n = int(input("enter the string:"))
# s = str(n)
# print(f" {s} is palindrome" if n == int(s[::-1]) else f" {s} is not a palindrome")


# leap year

# n = int(input('enter the year:'))
# print(f"{n} is a leap year" if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0 else f"{n} is not a leap year")
#         print(n, "leap year")
# elif n % 400 == 0:
#         print(n, "leap year")
# else:
#     print(n, "is not a leap")
#
#
# import calendar
#
# print(calendar.isleap(2012))

# perfect square
# n = 8
# if round(n ** 0.5) * round(n ** 0.5) == n:
#     print(f"{n} is perfect square number")
# else:
#     print(f"{n} is not a perfect square number")


# n = input("enter the charcter:")
# if "a" <= n <= "z" or "A" <= n <= "Z":
#     print(f"{n} is a alphabet")
# elif '0' <= n <= '9':
#     print(f"{n} is a number")
# else:
#     print(f" {n} is a spl character")

# if n.isalpha():
#     print(f"{n} is a alphabet")
# elif n.isdigit():
#     print(f"{n} is a number")
# else:
#     print(f"{n} is a spl character")

# n = int(input("enter the marks"))
# if n >= 60:
#     print("first class")
# elif n >= 35:
#     print("pass")
# else:
#     print("fail")


# starts with vowel

# s = input("enter the string")
# if s[0] in "aeiouAEIOU":
#     print(f"{s} starts with vowel")
# else:
#     print(f" {s} not starts with vowel")

# s = 264
# n = str(s)
# if int(n[0]) % 2 == 0:
#     print("even")
# else:
#     print("odd")

# n = 2468
# s = str(n)
# if int(s[-2]) % 2 != 0:
#     print("odd")
# else:
#     print("even")


# d = {"a": 1, "b": 2, "d": 4}
# key = len(d)
# if key % 2 == 0:
#     print(d)
# else:
#     d['c'] = 3
#     print(d)

# n = 564
# s = str(n)
# print("even number" if int(s[-2]) % 2 == 0 else "odd number")

# l = [1, 2, 3, 4, 5,6]
# print("even no" if len(l) % 2 == 0 else "odd no")


# a = [1,2,3]
# b = ['a','b','c']
# if a > b:
#     print('hai')

s = '    '
print(s.split())