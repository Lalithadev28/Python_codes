list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)


list3 = [5, 20, 15, 20, 25, 50, 20]

# list comprehension

# remove specific items and return a new list

val=20

res=[i for i in list3  if i != val]

print(res)


