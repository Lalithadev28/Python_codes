'''Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected output:

10 400
20 300
30 200
40 100 '''


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)