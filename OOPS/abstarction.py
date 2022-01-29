# from abc import ABC, abstractmethod
#
#
# class Bank(ABC):
#
#     def __init__(self):
#         self.bal = 20000
#
#     @abstractmethod
#     def balance(self):
#         pass
#
#     @abstractmethod
#     def deposit(self, amount):
#         pass
#
#     @abstractmethod
#     def withdraw(self, amount):
#         pass
#
#
# class Sbi(Bank):
#
#     def balance(self):
#         print(self.bal)
#
#     def deposit(self, amount):
#         self.bal += amount
#         self.balance()
#
#     def withdraw(self, amount):
#         self.bal -= amount
#         self.balance()
#
#
# c = Sbi()
# c.deposit(5000)
# c.withdraw(2000)


##################################################################################
# polymorphism wrt inbuilt function
s = 'hai'
len(s)              # no of char

l = [1, 2, 3, 4, 5]
len(l)              #no of ele

t = (1, 2, 3, 4, 5)
len(t)              #no of ele

s = {2,5,6,7,8}
len(s)              #no of keys

d = {'a':1, 'b':2, 'c':3}
len(d)              #no of keys


# polymorphism wrt operators

#addition

print(1+2)
print('1' + '2')

#substarction

print(3 -2)
print({1, 2, 3} - {2, 3})

#multiplication

print(2 * 3)
print([1, 2, 3] * 2)


# polymorphism wrt classmethods

class SBI:

    def balance(self):
        print('in sbi balance')

    def withdraw(self):
        print('in sbi withdraw')

class ICICI:

    def balance(self):
        print('in icici balance')

    def withdraw(self):
        print('in icici withdraw')


sbi = SBI()
icici = ICICI()

objects = (sbi, icici)

for obj in objects:
    obj.balance()
    obj.withdraw()

# polymorphism wrt inheritence


class Bank:

    def balance(self):
        print('in sbi balance')

    def withdraw(self):
        print('in sbi withdraw')


class ICICI(Bank):

    def balance(self):
        print('in icici balance')
        super().balance()

    def withdraw(self):
        print('in icici withdraw')
        super().withdraw()


b = Bank()
i = ICICI()
