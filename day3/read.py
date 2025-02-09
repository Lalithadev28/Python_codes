f=open("names.txt" ) # r mode is the default 
print(f.read())   # read() reads entire file 

f=open("names.txt" ) # r mode is the default 
print(f.readline())   # readline() reads oneline at  a time 
f.close()

