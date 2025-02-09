'''Union operation on Python Sets

Two sets can be merged using union() function or | operator. '''

a={1,2,3,4}
b={4,5,6}
c=a.union(b)
print(c)

d=a.union(b)  # union operator removes duplicates
print(c)
e =a | b    # union operator | removes duplicates
print(e)


'''Intersection operation on Python Sets

This can be done through intersection() or & operator.

common elements are selected'''

a={1,2,3,4}
b={4,5,6}
c=a.intersection(b)  # returns common elements 
print(c)
d =a & b             # returns common elements from both sets
print(d)



#s1 – s2	the set of elements in s1 but not s2


a={1,2,4,5}
b={4,5,6}
print(s1-s2)

s = set()  
print("The length of set is:", len(s))

# Adding element and tuple to the Set 
s.add(8) 
s.add(9) 
print("The length of set is:", len(s))

s.add((6, 7)) 
print("The length of set is:", len(s))