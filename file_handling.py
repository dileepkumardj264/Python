# with open('dj.txt') as fo:
#     count = 0
#     for line in fo:
#         a = line.split()
#         count += len(a)
#     print(count)


# with open('dj.txt') as f:
#     count = 0
#     for _ in f:
#         count += 1
#     print(count)

# with open('dj.txt') as f:
#     for index, line in enumerate(f, start=1):
#         if line.strip():
#             print(index, line)


# with open('dj.txt') as f:
#     a = list(f)
#     for line in reversed(a):
#         print(line)

# with open('dj.txt') as f:
#     for line in f:
#         print(len(line))


# fpath = r'C:\Users\Dileep\pythonProject24\newfiles\access-log.txt'
# with open(fpath) as f:
#     l = []
#     for line in f:
#         if line.strip():
#             a = line.split()
#             l.append(a[0])
# #
# d = {i: l.count(i) for i in l}
#
# x, *rest, y = sorted(d.items(), key=lambda item: item[-1])
# print(x, y)

# # TO EXTARCT IP ADDRESS FROM THE ACCESS LOG FILE
# fpath = r'C:\Users\Dileep\pythonProject24\newfiles\access-log.txt'
# with open(fpath) as f:
#     l = []
#     for line in f:
#         if line.strip():
#             a = line.split()
#             l.append(a[0])
#
# #USING DEFAULTDICT
# from collections import defaultdict
# d = defaultdict(int)
# count = 0
# for i in l:
#     d[i] += 1
# print(d)
#
# #WITHOUT USING BUITIN COUNT METHOD
# m = {}
# for i in l:
#     if i not in m:
#         m[i] = 1
#     else:
#         m[i] += 1
# print(m)
#
# # TO EXTRACT MESS FROM SAMPLE.LOG FILE
# path = r'C:\Users\Dileep\pythonProject24\newfiles\sample.log'
#
# with open(path) as fo:
#     mes = []
#     for line in fo:
#         if line.strip():
#             a = line.split()
#             mes.append(a[2])
# print(mes)
#
# # USING COUNT METHOD
# d1 = {i: mes.count(i) for i in mes}
# print(d1)
# x, *rest, y = sorted(d1.items(), key=lambda item:item[-1])
# print(x, y)
#
# # USING DEFAULT DICT
#
# d2 = defaultdict(int)
# for i in mes:
#     d2[i] += 1
# print(d2)
# x, *rest, y = sorted(d2.items(), key=lambda item:item[-1])
# print(x, y)
#
# # WITHOUT BUILTIN COUNT METHOD
#
# d3 = {}
# for i in mes:
#     if i not in d3:
#         d3[i] = 1
#     else:
#         d3[i] += 1
# print(d3)
# x, *rest, y = sorted(d2.items(), key=lambda item: item[-1])
# print(x, y)


# a = lambda x:x*2
# print(a((1,2)))
#
#
# def fac(n):
#     if n == 1:
#         return 1
#     return n * fac(n - 1)
#
#
# print(fac(10))


# with open(r'C:\Users\Dileep\pythonProject24\newfiles\sample.log') as f:
#     for line in f:
#         if line.strip():
#             b = line.split(' :')
#             print(b[1])


from collections import Counter, defaultdict
# with open(r'C:\Users\Dileep\pythonProject24\newfiles\sample.txt') as f:
#     count = 0
#     for line in f:
#         if line.strip():
#             for i in line:
#                 if i == ' ':
#                     count += 1
#     print(count)

# with open(r'C:\Users\Dileep\pythonProject24\newfiles\sample.txt') as f:
#     d = Counter()
#     for line in f:
#         if line.strip():
#             d += Counter(line)
#
#     print(d)

# with open(r'C:\Users\Dileep\pythonProject24\newfiles\sample.txt') as f:
#
#     d1 = defaultdict(int)
#     for line in f:
#         if line.strip():
#             for i in line:
#                 d1[i] += 1
#     print(d1)
#

# # WAP TO EXTARCT LIST OF COUNTRY NAME FROM FOOTBALL.TXT FILE

# with open(r'C:\Users\Dileep\pythonProject24\newfiles\football.txt', encoding='UTF8') as f:
#     l = []
#     for line in f:
#         if line.strip():
#             b = line.split()
#             l.append(b[1])
#
#
# # WAP TO PRINT MOST OCCURRING COUNTRY NAME ALONG ITS COUNT
# print(l)
# count_ = Counter(l)
# print(count_.most_common())


#WAP TO PRINT THE LINE NUMBER OF THE WORD GIVEN BY THE USER

# with open(r'C:\Users\Dileep\pythonProject24\newfiles\sample2.txt') as f:
#     word = input('enter the word:')
#     for index, line in enumerate(f, start=1):
#         if word in line:
#             print(index)

# with open(r'C:\Users\Dileep\pythonProject24\example1.txt', 'r') as f:
#     res = f.read()
#     print(res)
#     with open(r'C:\Users\Dileep\pythonProject24\example2', 'a') as f1:
#         f1.write(res)

# with open(r'C:\Users\Dileep\pythonProject24\example1.txt', 'w+') as f:
#     f.writelines(['apple\n', 'mango\n', 'flipkart\n', 'amazon\n'])
#     f.seek(0)
#     res = f.read()
#     print(res)
#     with open(r'C:\Users\Dileep\pythonProject24\example2', 'a') as f1:
#         f1.write(res)


import itertools

path = r"C:\Users\Dileep\pythonProject24\newfiles\sample.txt"


def sam(path, start, end):
    with open(path) as f:
        res = itertools.islice(f, start, end)
        print(list(res))


sam(path, 5, 9)

def last_line():
    with open(path) as f:
        line = 0
        for _ in f:
            line +=1
        f.seek(0)
        res = itertools.islice(f, line-2, line)
        print(list(res))


last_line()

from collections import deque


def saj(n):
    with open(path) as f:
        res = deque(f, n)
        print(list(res))


saj(1)
