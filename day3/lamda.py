x=[2,3,4,5]
y=[]
for i in x:
    va=i+2
    y.append(va)
print(x)
print(y)

#usng lamda
x=[2,3,4,5]
y=map(lambda a:a+2, x)
