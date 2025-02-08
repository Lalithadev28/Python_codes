import os

file_path = "C:\B4712\day6\sample.txt"
with open(file_path, 'w') as file:
    file.write("Hello, World!")

print(f"A new file has been created at {file_path}")