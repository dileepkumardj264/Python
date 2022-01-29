d = {}
e = dict([(2, 3), (5, 6), (6, 8)])
f = dict(a=1, b=2, c=4,)
g = dict({1: 2, 3: 4, 5: 6})
r = dict(d1=34, d2=65)
d[(23, 4)] = 'helllo'
print(d, e, f, g, r)
print(g.get(8, 'not there'))
print(g.items())
print(g.keys())
print(g.values())
print(e)
e = dict([(7, 8)])
print(e)
e[2] = 8
print(e)
e.update([(5, 3), (8, 9)], a=20)
print(e)
m = (dict.fromkeys(f, 12000))
print(m)
print(f)
print(m.pop('a'))
print(m)
m = {1: 2, 3: 4}
n = [1, 2, 3, 4]
p = dict.fromkeys(n, 200)
print(p)
q = {**f, **g}
print(q)
