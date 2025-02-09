#task1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dct=dict(zip(keys,values))
print(dct)

#tas2
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

#task 3
sampleDict = {"class": {"student": {"name": "Mike", "marks": {"physics": 70,"history": 80}}}}
print(sampleDict["class"]["student"]["marks"]["history"])

#task 4

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

employee_dict = dict.fromkeys(employees, defaults)
print(employee_dict)

# task 5
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
filtered_dict={}
filtered_dict = {key: value for key, value in sample_dict.items() if key in keys}
print(filtered_dict)

#task 6
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
rm_keys={key: value for key, value in sample_dict.items() if key not in keys}
print(rm_keys)

#task 7
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')

#task 8
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

#tas 9
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

min_value = min(sample_dict.values())

sample1_dict = {k: v for k, v in sample_dict.items() if v == min_value}

print(sample1_dict)

#task 10

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)