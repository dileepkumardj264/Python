s = 'hello'
import re
print(re.findall('hello', s))                       #['hello']

s = 'hello how are you how you doing'
print(re.findall('how', s))                         #['how', 'how']

s = 'hello how are you How you doing'
print(re.findall('h\w+', s, re.IGNORECASE))          #['how', 'How']

print(re.findall('.', 'annna'))                     #['a', 'n', 'n', 'n', 'a']

print(re.findall('a.', 'annna'))                    #['an']

print(re.findall('.a', 'annna'))                #['na']

print(re.findall('a...a', 'annna'))             #['annna']

print(re.findall('a.a', 'annna'))               #[]

print(re.findall('.+', 'annna'))                #['annna']

print(re.findall('a.+a', 'annna'))              #['annna']

print(re.findall('a+a', 'annna'))               #[]

print(re.findall('.', 'annna'))                 #['a', 'n', 'n', 'n', 'a']

print(re.findall('a*a', 'annna'))               #['a', 'a']

print(re.findall('he*o', 'hello'))              #[]

print(re.findall('he*o', 'heeeo'))              #['heeeo']

print(re.findall('he*o', 'heo'))                #['heo']

print(re.findall('^hello', 'hello world'))       #['hello'] to check startwith

print(re.findall('hello$', 'world hello'))        #['hello'] to check ends with

print(re.findall('an?a', 'ana'))                    #['ana']


# wap to count the no of vowels in the given string
print(len(re.findall('[aeiou]', 'hello world')))         #['e', 'o', 'o']  len will give count 3

print(re.findall('[0123456789]', 'this is pen of rs 100'))      #['1', '0', '0']

print(re.findall('[0123456789]+', 'this is pen of rs 100'))     #['100']

print(re.findall('[0-9]+', 'this is pen of rs 100'))            #['100']

print(re.findall("\d+", 'this is pen of rs 100'))             #['100']

print(re.findall('\D+', 'this is pen of rs 100'))             #['this is pen of rs ']

s = 'Hi How are you'
print(re.findall('.*', s))                                      #['Hi How are you', '']

print(re.findall('.', s))           #['H', 'i', ' ', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u']

print(re.findall('.+', s))          #['Hi How are you']

print(re.findall('[a-z]+', s))      #['i', 'ow', 'are', 'you']

print(re.findall('[a-zA-Z]+', s))   #['Hi', 'How', 'are', 'you']

print(re.findall('[\w]+', s))          #['Hi', 'How', 'are', 'you']

s = 'Hi_How are you'

print(re.findall('[\w]+', s))       #['Hi_How', 'are', 'you']


print(re.findall('[\W]+', s))          #[' ', ' ']

print(re.findall('[\s]+', s))           ##[' ', ' ']

print(re.findall('[\S]+', s))           #['Hi_How', 'are', 'you']

print(re.findall('\d+', '560043'))      #['560043']

print(re.findall('\d+', '5600432255'))      #['5600432255']

print(re.findall('\d{6}', '5600432255'))        #['560043']

print(re.findall('\d{6}$', '5600432255'))       #['432255']

print(re.findall('^\d{6}$', '5600432255'))         #[]

print(re.findall('^\d{6}$', '5600'))                #[]

s= 'hai how are you hello'
a = s.split()
for i in a:
    if i[0] == 'h':
        print(i)

print(re.findall('h\w+', s))                #['hai', 'how', 'hello']

print(re.findall('h\w', s))                 #['ha', 'ho', 'he']


s = 'Happy Birthday to you'
print(re.findall('\w+y', s))                #['Happy', 'Birthday']

s = 'sony12pvt43ltd798'
print(re.findall('\d+', s))
res = (re.findall('\d+', s))
total = 0
for i in res:
    total += int(i)
print(total)                    #853

out = (re.findall('\d', s))
sum = 0
for i in out:
    sum += int(i)
print(sum)                              #34


# WAP to count the no whitespaces in the given string
s ='hai hello how are you'
space = re.findall('\s', s)
print(len(space))


# WAP to count the no of whitespaces present in a file:
path = r'C:\Users\Dileep\pythonProject24\newfiles\sample.txt'

with open(path) as f:
    total = 0
    for line in f:
        for i in line:
            if i == ' ':
                total += 1
    print(total)

with open(path) as f:
    count = 0
    for line in f:
        res = len(re.findall(' ', line))
        count += res
    print(count)


# WAP to count the of occurences of a particular word in a string
s = 'hi hello how are you'
a = s.split()
d = {}
for i in a:
    d[i] = a.count(i)
print(d)


out = len(re.findall('how', s))
print(out)

# WAP to count the no of occurences of a particular word in a file

with open(path) as f:
    count = 0
    for line in f:
        a = line.split()
        for i in a:
            if i == 'hello':
                count += 1
    print(count)

with open(path) as f:
    total = 0
    for line in f:
        out = len(re.findall('hello', line))
        total += out
    print(total)
#WAP to count the no of occrences of non special characters in the given string
s = 'hello@world!! welcome!!! to& python***'
print(len(s))
out = re.findall('\w', s)
print(out)
print(len(out))


# for the same string count the no of spl chr in the above string
res = re.findall('\W',s)
print(res)
print(len(res))

# filter only those chr except digit
st = 'sony@12pvt%%43ltd##798!!!'
ch = re.findall('\D', st)
print(ch)

#WAP to count the no of chr in each word and create a dict of word and its len pair(ignore spl chr)
sa = 'hello@ world:) welcome!!! to python:):)'
chr = re.findall('\w+',sa)
print({i:len(i) for i in chr})

#WAP to count the no of upper case and lower case letters in the given string
s = 'HaiHEllo'
u = re.findall('[A-Z]', s)
l = re.findall('[a-z]', s)
print(len(u), len(l))


#YYYY-MM-DD
dates = ["2019-01-02", '2019-13-08', '2021-12-26', '2022-01-32']

# for i in dates:
#     print(re.findall(r'\d{4}-(?:0[1-9]|1[012])-(?:0[1-9]|[12][0-9]|3[01])', i))

date = ["02-01-1999", '04-04-2021', '26-04-1989', '30-09-1994']

for i in date:
    out = re.findall(r'(?:0[0-9]|[12][0-9]|3[01])-(?:0[1-9]|1[012])-\d{4}', i)
    print(out)


s = 'hello how are you'
print(re.findall('\w+', s))


email = ['dileep@gmail.com', 'yogi@yahoo.in']
for i in email:
    out = re.findall(r'\w+@\w+.\w+', i)
    print(out)

s = 'python is a programming langauge, programming is fun'
b = s.find('programmimg')
while b != -1:
    print(b)
    b = s.find('programming', b+1)


# m = 0
# while m < len(s):
#     a = s.index('programming', m)
#     print(a)
#     m = a + 1

# to replace vowels with '*'
print(re.sub(r'[aeiou]', '*', s))


# to replace spl chr with -
s = 'hi#%^^&hfpeo&*(jojo'

print(re.sub(r'[\W_]', '-', s))


path = r'C:\Users\Dileep\pythonProject24\newfiles\sample2.txt'
with open(path) as f:
    for line in f:
        a = re.sub(r'python', 'java', line)
        print(type(a))

# Write a pro to print only the starts with vowel
s = 'every day is not a sunday'

print(re.findall(r'\b[aeiou]\w*', s))

s = 'python is a programming langauge, programming is fun'

print(re.subn('is', 'are', s))          #no of times replaced

print(re.match('python', s))           #used to match word which is in first

print(re.search('python', s))           #used to search word in the string

s = 'hai hello how are you, how you doing'

print(re.match('hai',s))

r = (re.search('how', s))
print(r.start(), r.end())
print(r.span())
print(r.pos)
print(r.endpos)
print(re.findall('how', s))
print(re.findall('h+w', s))

s = 'dileepkumar.dj@gmail.com hello how are you abc@yahho.com 123@fb.in sathya@gamil., dileep.dj@yahoo.co.in'
print(re.findall(r'\w+\.?\w*@\w+\.?\w*\.[A-Za-z]{2,3}', s))


s = 'hEllo how Are yhoau'

print(re.findall(r'\bh\w+',s))
print(re.findall(r'\b[aeh]\w',s))

out = re.finditer('h\w+', s, 2)
print(out)
for i in out:
    print(i.span())

res = re.sub(r'[aeiouAEIOU]', '*', s)
print(res)
