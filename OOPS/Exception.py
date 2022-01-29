class EmptyLineError(Exception):
    pass

fpath = r'C:\Users\Dileep\pythonProject24\newfiles\sample.txt'

with open(fpath) as f:
    line_no = int(input('enter the line no:'))
    for index, line in enumerate(f, start=1):
        if index == line_no:
            a = line.split()
            if line.strip():
                print(line)
                print(len(a))
            else:
                print(len(a))
                raise EmptyLineError ('line is empty')