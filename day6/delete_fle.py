import os

file_to_delete = "C:\B4712\day6\example.txt"

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"The file {file_to_delete} has been deleted.")
else:
    print("The file does not exist.")