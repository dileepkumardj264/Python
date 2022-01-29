# class Vehicle:
#
#     speed = 0
#     passenger = 1
#     fuel_type = ''
#
#     def go(self):
#         print('in go')
#
#     def stop(self):
#         print('in stop')
#
#     def change_Direction(self):
#         print('in change direction')
#
#
# class Car(Vehicle):
#
#     model_type = 'xyz'
#     Doors = 4
#     automaker = 'maruthi'
#
#     def radio(self):
#         print('no body touches my radio')
#
#     def windshildwiper(self):
#         print('in wiper')
#
#     def change_Direction(self):
#         print('in car change direction')
#
#
# c = Car()
# c.change_Direction()
# c.go()
#
#####################################################################

# class Product:
#
#     def __init__(self, name, price, discount_percent):
#         self.name = name
#         self.price = price
#         self.disc = discount_percent
#
#     def getDiscountAmount(self):
#
#         amount = self.price * (self.disc) // 100
#         print(amount)
#
#     def getDiscountPrice(self):
#
#         Dprice = self.price - (self.price * (self.disc) // 100)
#         print(Dprice)
#
#     def PrintDescription(self):
#         print(self.price)
#         self.getDiscountAmount()
#         self.getDiscountPrice()
#
#
# c = Product('xyz', 250, 10)
#  b
#
# class Book(Product):
#
#     def __init__(self, name, price, discount_percent, author):
#         super().__init__(name, price, discount_percent)
#         self.author = author
#
#     def getDiscountAmount(self):
#         super().getDiscountAmount()
#
#     def getDiscountPrice(self):
#         super().getDiscountPrice()
#
#     def PrintDescription(self):
#         super().PrintDescription()
#
#
# class Movie(Product):
#
#     def __init__(self, name, price, discount_percent, year):
#         super().__init__(name, price, discount_percent)
#         self.year = year
#
#     def PrintDescription(self):
#         super().PrintDescription()
#
#
# n = Movie('kariya', 200, 10, 2012)
# n.PrintDescription()
#
#
#


###################################################################################################


# class A:
#
#     __a = 10
#     b = 20
#
#     def display(self):
#         print(self.__a, self.b)
#
#
# class B(A):
#
#     c = 30
#
#     def display(self):
#         super().display()
#         print(self.c)
#
#
# c = B()
# c.display()

#############################################################################


# class Bank:
#
#     Bname = 'SBI'
#     MBL = 'Mysore'
#
#     def __init__(self, name, phoneno, addr):
#         self.name = name
#         self.phone = phoneno
#         self.addr = addr
#
#     def display(self):
#         print(self.name, self.phone, self.addr)
#
#
#
#
# class Bank2(Bank):
#
#     def __init__(self, name, phoneno, addr, adhar, pan, email):
#         super().__init__(name, phoneno, addr)
#         self.adhar = adhar
#         self.pan = pan
#         self.email = email
#
#     def display(self):
#         super().display()
#         print(self.adhar, self.pan, self.email)
#
#
#
#
# c = Bank('dileep', 9886144850, 'bang')
# c1 = Bank2('divya', 8648644499, 'mys', 89444916454163, 'csfw34245d', 'ddjwui')
#
# c.display()
# c1.display()

###############################################################################################

class A:

    def __init__(self, a, b, c, f, g):
        self.a = a
        self.b = b
        self.c = c
        self.f = f
        self.g = g

    def display(self):
        print(self.a, self.b, self.c)

class B:

    def __init__(self, d, e):
        self.d = d
        self.e = e

    def display(self):
        print(self.d, self.e)

class C(B, A):

    def __init__(self, a, b, c, d, e):
        super().__init__(a, b, c, d, e)

