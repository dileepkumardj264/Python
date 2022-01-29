import csv
# with open(r'C:\Users\Dileep\pythonProject24\newfiles\test.csv') as f:
#     rows = csv.reader(f)
#     for line in rows:
#         print(line)
#
# with open(r'C:\Users\Dileep\pythonProject24\newfiles\test.csv') as f:
#     drows = csv.DictReader(f)
#     for line in drows:
#         print(line)

# path = r'C:\Users\Dileep\pythonProject24\newfiles\example.csv'
# with open(path, 'a') as f:
#     dict_writer_object = csv.DictWriter(f, ['age', 'name', 'salary'])
#     dict_writer_object.writerow({'name': 'ram', 'age': 30, 'salary': 20000})
#     dict_writer_object.writerows([{'name': 'dileep', 'age': 32, 'salary': 40000}, {'name': 'ramesh', 'age': 38, 'salary': 250000}])
#
#
# fpath = r'C:\Users\Dileep\pythonProject24\newfiles\test.csv'
#
# with open(fpath,'a') as f1:
#     writer_object = csv.writer(f1)
#     writer_object.writerow(['TESLA', 100, 23.25])
#     writer_object.writerows([('ACME', 100, 12.2), ('FB', 200, 25), ('MRF', 50, 200)])


path = r'C:\Users\Dileep\pythonProject24\newfiles\vaccination_data.csv'

# with open(path, 'r') as f:
#     file = csv.reader(f)
#     d = {}
#     total = 0
#     for line in file:
#         if line[5].isdigit():
#             d[line[0]] = line[5]
#             total += int(line[5])
#     print(total)
#     print(d)
#
# with open(path, 'r') as f:
#     file = csv.reader(f)
#     d1 = {}
#     for line in file:
#         d1[line[0]] = line[2]
#     print(d1)
#
# with open(path, 'r') as f:
#     file = csv.reader(f)
#     d2 = {}
#     for line in file:
#         if line[6].isdigit():
#             d2[line[0]] = line[6]
#     print(d2)
#     out = sorted(d2.items(), reverse=True, key=lambda item:int(item[-1]))
#     print(out[:3])
#
# with open(path, 'r') as f:
#     file = csv.reader(f)
#     d3 = []
#     count = 0
#     for line in file:
#         if line[6].isdigit():
#             if int(line[6]) < 10000:
#                 count += 1
#                 d3.append(line[0])
#     print(d3)
#     print(count)
#
# with open(path, 'r') as f:
#     file = csv.reader(f)
#     l3 = []
#     for line in file:
#         l3.append(line)
#     print(l3[-1][0], l3[-1][5], l3[-1][6])

# from collections import Counter, defaultdict
# d = defaultdict(int)
# d1 = defaultdict(list)
# with open(path) as f:
#     csv_dict_file = csv.DictReader(f)
#     for i in csv_dict_file:
#         for key, value in i.items():
#             if value.isdigit():
#                 d[key] += int(value)
#             else:
#                 d1[key] += [value]
#
# print(d)
# print(d['TOTAL_VACCINATIONS'])
# print(d1)
