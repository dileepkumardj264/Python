# # create object methods using constructor
#
# class Employee:
#     fname = 'steve'
#     lname = 'jobs'
#
#     def __init__(self, name, age):
#         self.a = name
#         self.b = age
#
#
# emp1 = Employee('dileep', 32)
# emp2 = Employee('ramesh', 34)
#
# print(emp1.__dict__)
# print(emp1.a, emp1.b)
#
# # print(Employee.a)    # Attribute Error (cant access the object attributes using class name)

###############################################################
# # creating  object variable with class variable
# class Employee:
#     fname = 'steve'
#     lname = 'jobs'
#
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
# emp1 = Employee('Tata', 'Birla')
# emp2 = Employee('Ambani', 'Mukesh')
#
# print(emp1.__dict__)
# print(emp2.__dict__)
# print(Employee.__dict__)
# print(emp1.fname)
# print(Employee.fname)
#
################################################
# class Numbers:
#     a = 10
#     b = 20
#
#     def __init__(self, c, d):
#         self.c = c
#         self.d = d
#
#     def display(self):
#         print(self.a, self.b, self.c, self.d)
#
#
# n = Numbers(30, 40)
# print(n)
# print(Numbers)
# Numbers.display(n)

##############################################
# class Sample:
#     a = 10
#     b = 20
#
#     def add(self):
#         res = self.a + self.b
#         print(res)
#
#
# n = Sample()
# n.add()


###################################################

# class Student:
#     def __init__(self, sname, sid, sdob):
#         self.a = sname
#         self.b = sid
#         self.c = sdob
#
#     def check(self):
#         date, month, year = self.c.split('/')
#         if abs(int(year)) - 2021 > 18:
#             print(f'{self.a} is above 18 years')
#         else:
#             print(f'{self.a} is below 18 years')
#
#
# s1 = Student('ramesh', '1234', '01/04/1989')
# s1.check()

#################################################

# class BankAccount:
#
#     owner = 'String'
#     balance = 0
#
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print('Transaction Successful')
#         print(f'{self.balance} balance after deposit')
#
#     def withdrawal(self, amount):
#         if self.balance >= amount:
#             self.balance = self.balance - amount
#             print('Transaction successful')
#             print(f'{self.balance} balance after withdrawal')
#
#
# c1 = BankAccount()
# c1.deposit(10000)
# c1.withdrawal(5000)

###################################################################
# from math import pi
# class Circle:
#     x_co = 4.4
#     y_co = 5.6
#     radius = 10.0
#
#     def find_area(self):
#         area = pi * self.radius ** 2
#         print(f'area of the circle is {area}')
#
#     def find_circumference(self):
#         circumference = 2 * pi * self.radius
#         print(f'the circumference of circle is {circumference}')
#
#
# a = Circle()
# a.find_area()
# a.find_circumference()


#################################################################

# class ListData:
#
#     list = [1, 2, 3, 4, 5]
#
#     def add_data(self, ele):
#         self.list.append(ele)
#         print(self.list)
#
#     def delete_data(self, ele):
#         if ele in self.list:
#             self.list.remove(ele)
#             print(self.list)
#         else:
#             print('no such element')
#
#     def find_length(self):
#         print(len(self.list))
#
#     def find_data(self, ele):
#         if ele in self.list:
#             print(self.list.index(ele))
#         else:
#             print('no such element')
#
#
# a = ListData()
# a.add_data(10)
# a.delete_data(3)
# a.find_length()
# a.find_data(10)


####################################################################
#
# class Books:
#     book_data = {}
#
#     def add_book(self, book_name, book_author, book_id, year_of_publish, price):
#         self.book_data[book_name] = {'book_author': book_author, 'book_id': book_id, 'year_of_publish': year_of_publish, 'price': price}
#
#     def delete_book(self, key):
#         print(self.book_data.pop(key))
#
#     def display_book(self):
#         print(self.book_data)
#
#     def inquire_book(self, key):
#         print(self.book_data[key])
#
# c = Books()
# c.add_book('Harry potter', 'dileep', 123, '2021', 200)
# c.add_book('abc', 'XTYZ', 234, '1989', 2000)
# print(c.book_data)
# c.display_book()
# c.delete_book('abc')
# c.inquire_book('Harry potter')


# a = [10, 20]
# b = a
# b += [30, 40]
# print(a)
# print(b)

######################################################3
# class Person:
#
#     d = {}
#
#     def __init__(self, *details):
#         for name, birthdate in details:
#             self.d[name] = birthdate
#
#     def get_name(self, name):
#         if name in self.d:
#             print(self.d[name])
#         else:
#             print(f'{name} is not in list')
#
#     def set_name(self, name, birthdate):
#         self.d[name] = birthdate
#
#     def is_birthdate(self,name,birthdate):
#         if self.d[name] == birthdate:
#             return True
#         else:
#             return False
#
#
# p1 = Person(('mahesh', '30/07/1998'), ('dileep', '26/04/1989'), ('ramesh', '14/08/1988'))
#
# print(p1.d)
# p1.get_name('dileep')
# print(p1.is_birthdate('dileep', '24/04/1989'))
# p1.set_name('yogesh', '13/05/1989')
# print(p1.d)

#######################################################
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.sal = salary

    def display(self):
        print(self.name, self.sal)

    @classmethod
    def spam(cls):
        e1 = cls('shyam', 20000)
        e1.display()

    @staticmethod
    def addition(a, b):
        return a + b


e = Employee('ram', 25000)
e.spam()
print(e.addition(2, 3))
print(Employee.addition(3, 4))
print(e)

############################################################
# class Employee:
#
#     def __init__(self):
#         self.a = 10
#
#     def __call__(self, b, c):
#         return self.a + b + c
#
#
# e = Employee()
# print(e(5, 6))



####################################################
# TO PRINT HELLOEVERYONE

# class Greeting:
#
#     def __call__(self):
#         print('helloeveryone')
#
#
# g = Greeting()
# g()

#################################################################

# create a callable object to check the number is even or odd

# class Numbers:
#
#     def __call__(self, n):
#         if n % 2 == 0:
#             return 'Even'
#         return 'False'
#
#
# e = Numbers()
# print(e(20))


################################################
# create a callable object to check if the given two string are anagrams or not

# class Anag:
#
#     def __call__(self, s1, s2):
#         if sorted(s1) == sorted(s2):
#             return 'two strings are anagrams'
#         return 'two strings are noe anagrams'
#
#
# e = Anag()
# print(e('fired', 'fried'))


###############################################################
# write a class decorator to print a message after executing any function
# def times(n):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#                 print('hai hello everyone')
#         return wrapper
#     return outer
#
#
# @times(3)
# def display():
#     print('good morning')
#
#
# display()

#######################################################
# class log:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             for _ in range(self.n):
#                 func(*args, **kwargs)
#                 print('hai hello everyone')
#
#         return wrapper
#
# @log(4)
# def display():
#     print('good morning')
#
#
# display()
#
# @log(5)
# def add(a, b):
#     print(a+b)
#
#
# add(2, 3)
# ######################################################3
#
#
# def mess(msg = 'good afternoon'):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             func()
#             print(msg)
#         return wrapper
#     return outer
#
# @mess()
# def display():
#     print(2)
#
#
# display()
#
# ##########################################################
# class log:
#     def __init__(self, msg= 'good afternoon'):
#         self.msg = msg
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print(self.msg)
#             func()
#         return wrapper
#
# @log('hai hello')
# def display():
#     print(2)
#
# display()

###################################################


# class Reverse:
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res[::-1]
#         return wrapper
#
#
# @Reverse()
# def rev(s):
#     return s
#
#
# print(rev('hai'))


#############################################
#
# class Count:
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print(len(args) + len(kwargs))
#             func(*args, **kwargs)
#         return wrapper
#
# @Count()
# def sam(*args, **kwargs):
#     return args
#
#
# sam(1, 2, 3, a=4, b=5, c=6)

#######################################################

# class typer:
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             for i in args:
#                 if not(isinstance(i, int)):
#                     return 'invalid input'
#             else:
#                 return func(*args, **kwargs)
#         return wrapper
#
# @typer()
# def add(a, b, c):
#     return a + b + c
#
#
# print(add(2, 3, 4))


######################################################
import typing


# class TypeCheck:
#
#     def __init__(self, *type_):
#         self.a = type_
#
#     def __call__(self,func):
#         def wrapper(*args):
#             for i, j in zip(args, self.a):
#                 if not(isinstance(i, j)):
#                     print(f'{i} is not a type of {j}')
#             else:
#                 res = func(*args)
#                 return res
#         return wrapper
#
#
# @TypeCheck(int, str, int)
# def sam(a, b, c):
#     return str(a) + b + str(c)
#
#
# print(sam(1, '2', 3))


class Name:

    a = 10
    b = 20


d = Name()
print(callable(d))
