'''Task :

Find the biggest of the arguments passed in the command line shell of the operating system

 12 45 67 9 8

Ouput value :

 Max is  : 67'''


import sys
# total arguments
n = len(sys.argv)
bigger=int(sys.argv[1])
for i in range(2, n):
    if bigger < int(sys.argv[i]):
       bigger=int(sys.argv[i])
print("\n\nBiggest :", bigger)
