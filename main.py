s=('hello',123,2456,'hai',4674,869)
out=()
for i in s:
    if type(i)==int:
        res=0
        for j in str(i):
            res+=int(j)
        out+=(str(res),)
    else:
        out+=(i,)
print(out)