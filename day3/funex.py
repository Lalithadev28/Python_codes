def netamt(amt, gst=18):     # default value , it is taken when we dont pass value
    return amt+amt*gst/100
    
print("Laptop price " , netamt(40000))  
print("Cake         " , netamt(300, 5))


def netamt(amt, gst=18):  # default value , it is taken when we dont pass value
    return amt+amt*gst/100
    
print("Laptop price " , netamt(40000))  
print("Cake         " , netamt(300, 5))
print("Food Items   " , netamt(500, 7))

def addtwo(x,y):
    return x+y 
def prodtwo(x,y):
    return x*y
    
a=int(input("Enter values for a ")) 
b=int(input("Enter values for b "))

print("Sum   " , addtwo(a,b))
print("Prod  " , prodtwo(a,b))