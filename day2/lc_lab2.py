fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if len(x) == 4 or len(x) == 5 ]
print(newlist)
