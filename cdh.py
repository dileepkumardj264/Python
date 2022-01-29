for m in range(1,1000):
    out=''
    for i in str(m):
        out+=str(int(i)**len(str(m)))
        print(out)
    if out==m:
        print(m)