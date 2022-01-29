
# class Public:
#     name = 'Ram'
#
#     def display(self):
#         print(self.name)
#
#
# p = Public()
# print(p.name)
# p.display()
#
#
# class PublicChild(Public):
#
#     def spam(self):
#         print('in child class')
#         self.display()
#
#
# c = PublicChild()
# print(c.name)
# c.display()
# c.spam()

##################################################################

# class Protected:
#
#     _name = 'Sita'
#
#     def _display(self):
#         print('name is:', self._name)
#
#
# p = Protected()
# print(p._name)
# p._display()
#
# class Child(Protected):
#
#     def spam(self):
#         print(self._name)
#         self._display()
#
# c = Child()
# print(c._name)
# c._display()
# c.spam()

##############################################################
#
# class Private:
#
#     __name = 'laki'
#
#     def __display(self):
#         print('in class private', self.__name)
#
#
#
# p = Private()
# print(p.__name())               #AttributeError     _Private__name: 'laki'
#
# class Child(Private):
#
#
#     def spam(self):
#         print(self.__name)        #_Child__name
#
# c = Child()
# print(c.__name())               #AttributeError
# c.spam()                        #AttributeError         _Child__name

####################################################################################3

# class BankAccount:
#
#     __roi = 4.5
#
#     def display(self):
#         print(self.__roi)
#
# class SavingAccount(BankAccount):
#
#     __roi =  2.5
#
#     def spam(self):
#         print(self.__roi)
#
# c = SavingAccount()
# c.spam()


###################################################################################

# class Student:
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks
#
#     def display_marks(self):                #getter
#         return self.__marks
#
#     def change_marks(self, new_value):      #setter
#         self.__marks = new_value
#
#     def delete_marks(self):                 #deleter
#         del self.__marks
#
#     marks = property(display_marks, change_marks, delete_marks)
#
#
# s = Student('Tom', 60)
# print(s.marks)
# s.marks = 75
# print(s.marks)
# del s.marks
# print(s.marks)


##################################################################

# class Student:
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks
#
#         @property
#         def marks(self):
#             return self.__marks
#
#         @marks.setter
#         def marks(self, new_value):
#             self.__marks = new_value
#
#         @marks.deleter
#         def marks(self):
#               del self.__marks
#
# s = Student('dileep', 65)
# s.marks = 90
# print(s.marks)

#############################################################

# class Account:
#
#     def __init__(self, bank, bal, acc):
#         self.bank = bank
#         self.__bal = bal
#         self.__acc = acc
#
#     @property
#     def balance(self):
#         return self.__bal
#
#     @balance.setter
#     def balance(self, new_value):
#         raise TypeError ('balance cannot be changed')
#
#     @property
#     def account(self):
#         return self.__acc
#
#     @account.setter
#     def account(self, new_value):
#         raise TypeError ('Account num cannot be modified')
#
# s = Account('canara', 20000, 2889048485)
# print(s.balance)
# print(s.account)
# s.account = 24246467878


##############################################################################

class Student:

    def __init__(self, sname, phy_marks, che_marks, bio_marks):
        self.__sname = sname
        self.__phy_marks = phy_marks
        self.__che_marks = che_marks
        self.__bio_marks = bio_marks

    @property
    def Student_name(self):
        return self.__sname

    @Student_name.setter
    def Student_name(self, new_name):
        self.__sname = new_name

    @property
    def Phy_marks(self):
        return self.__phy_marks

    @Phy_marks.setter
    def Phy_marks(self, new_marks):
        self.__phy_marks = new_marks


    @property
    def Che_marks(self):
        return self.__che_marks

    @Che_marks.setter
    def Che_marks(self, new_marks):
        self.__che_marks = new_marks

    @property
    def Bio_marks(self):
        return self.__bio_marks

    @Bio_marks.setter
    def Bio_marks(self, new_marks):
        self.__bio_marks = new_marks

    def display(self):
        print(self.__sname, self.__phy_marks, self.__che_marks, self.__bio_marks)


    def Percentage(self):
        print(self.__phy_marks, self.__che_marks, self.__bio_marks)
        print((self.__phy_marks + self.__che_marks + self.__bio_marks) / 300 * 100)


s = Student('dileep', 65, 75, 85)
s.Student_name = 'Kumar'
s.Bio_marks = 95
s.Che_marks = 94
s.Phy_marks = 96
s.display()
s.Percentage()

