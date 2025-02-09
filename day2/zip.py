names = ['John', 'Alice', 'Bob', 'Lucy']

scores = [85, 90, 78, 92]

res = zip(names, scores)
print(list(res))


'''Given

list1 = [10, 20, 30, 40]

list2 = [100, 200, 300, 400]

Expected output:

10 400
20 300
30 200
40 100'''

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)



'''Given:

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][0] is 300

Expected output:

[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]'''

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

