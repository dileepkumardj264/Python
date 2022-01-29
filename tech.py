# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([j for i in l for j in i])

# for i in range(1, 5):
#     print("* " * i)
#
# for i in range(4, 0, -1):
#     print("* " * i)

# for i in range(1, 6):
#     print(f'{"* " * i:>10}')

# for i in range(5, 0, -1):
#     print(f'{"* " * i:^12}')

# pat = ' '
# for i in range(1, 5):
#     pat += str(i) + ' '
#     print(f'{pat:>10}')

# pat = ''
# for i in range(ord('a'), ord('e')+1):
#     pat += chr(i) + " "
#     print(pat)
#
# out = ''
# for i in range(ord('e'), ord('a')-1, -1):
#     out += chr(i) + " "
#     print(out)

# for i in range(1, 5):
#     print('* ' * i)
#     print('*')
# l = [1, 2, 3, 4, 5]
# print('list has odd no of elements' if len(l) % 2 != 0 else 'list has even no of elements')
#
# print([j ** i for i, j in enumerate(l)])
# s = 'hello12345world'
# print({i: s.count(i) for i in set(s)})
# print([i for i in s if i.lower() in 'aeiou'])
# print([i for i in s if i.isdigit()])
# print(list(zip(l, s)))

# l = ['facebook.com', 'gmail.in', 'yahoo.co']
# print([(i, len(i)) for i in l])
# print([(i[0], i) for i in l])
#
# d = {'f': 'facebook', 'g': 'gmail', 'y': 'yahoo'}
# print([(i, j) for i, j in enumerate(d.items())])
#
# print([i.split('.')[-1] for i in l])
#
#
# print([i * j for i in range(1, 3) for j in range(1, 3)])

# for i in range(1, 6):
#     print(f'{"* " * i:^10}')

s = ''
for i in range(ord('A'), ord('D')+1):
    print(chr(i))
    s += chr(i) + " "
    print(s)

for i in range(1, 5):
    print(f'{"* " * i:>10}')

m = ''
for j in range(ord('a'), ord('e')+1):
    m += chr(j) + " "
    print(f'{m:^12}')
