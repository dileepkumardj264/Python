import pickle

a = 'hello'

pic_obj = pickle.dumps(a)
print(pic_obj)

py_obj = pickle.loads(pic_obj)
print(py_obj)

with open('sample.pkl', 'wb') as f:
    pickle.dump(a, f)

with open('sample.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)

path = r'C:\Users\Dileep\pythonProject24\newfiles\sample.txt'
with open(path) as f:
    res = f.read()
    with open('sample.pkl', 'wb') as file:
        pickle.dump(res, file)
