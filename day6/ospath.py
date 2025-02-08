import os
 
file_path = "C:\B4712\day1\lab5.py"
 
if os.path.exists(file_path):
 
    print("The file exists!")
 
else:
    print("The file does not exist.")