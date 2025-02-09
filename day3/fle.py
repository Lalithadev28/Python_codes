f=open("names.txt", "w") 
for i in range(5):
    name=input("Enter name   ")
    f.write(name+"\n") 

f.close()    
