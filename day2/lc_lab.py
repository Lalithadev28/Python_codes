fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist1 = [x for x in fruits if x != "apple"]

print(newlist1)