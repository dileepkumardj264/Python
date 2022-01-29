#wap to print the statement hello world 5 times

# for _ in range(5):
#     print("Hello World")

# WAP TO PRINT THE EVEN NUMBERS FROM 1 TO 10

# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)
#
# for i in range(2,11,2):
#     print(i)

# WAP TO PRINT THE ODD NUMBERS BETWEEN THE RANGE 20 TO 40
# for i in range(21,41,2):
#     print(i)
#
# for i in range(21,41):
#     if i % 2 != 0:   # if i % 2:      #  if not i % 2 == 0:
#         print(i)

# WAP TO PRINT THE NUMBERS WHICH ARE DIVISIBLE BY 4 IN RANGE 1 TO 50

# for i in range(2,51):
#     if i % 4 == 0:
#         print(i)

# WAP TO PRINT THE NUMBERS WHICH ARE DIVISIBLE BY BOTH 4 AND 7 BETWEEN 1 TO 50:

# for i in range(1,101):
#     if i % 4 == 0 and i % 7 == 0:
#         print(i)

# WAP TO CHECK WHETHER THE NUMBER GIVEN FROM THE USER IS PRIME OR NOT

# n = int(input('enter the number:'))
# flag = 0
# for i in range(2,n):
#     if n % i == 0:
#         flag = 1
# if flag == 0:
#     print('prime')
# else:
#     print('non prime')

# for i in range(2,n):
#     if n % i == 0:
#         print("not a prime")
#         break
# else:
#     print('prime number')

# for i in range(2,n):
#     if i % 2 == 0:
#         flag = 1
#         break
#     else:
#         continue
# if flag == 0:
#     print("prime no")
# else:
#     print("non prime")

# for i in range(2,n):
#     if i % 2 == 0:
#         flag = 1
#         break
#     else:
#         pass
# if flag == 0:
#     print("prime no")
# else:
#     print("non prime")

# for n in range(2,20):
#     for i in range(2,n):
#         if n % i == 0:
#             break
#     else:
#         print(n,end = ' ')
