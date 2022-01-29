def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
def get():
    a=int(input('enter the value'))
    b=int(input('enter the value'))
    return a,b
a,b=get()
print('sum is',add(a,b))
print('diff is',sub(a,b))