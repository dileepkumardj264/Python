import json

a = None
json_obj = json.dumps(a)
print(json_obj)

s = "hello"
json_obj = json.dumps(s)
print(json_obj)

l = ['hello', 'hai']
json_obj = json.dumps(l)
print(json_obj)

m = {'a': 2, 'b': 3}
json_obj = json.dumps(m)
print(json_obj, type(json_obj))

py_obj = json.loads(json_obj)
print(py_obj, type(py_obj))


with open("sample.json", 'w') as file:
    json.dump(m, file)


with open('sample.json') as file:
    data = json.load(file)
    print(data)
    