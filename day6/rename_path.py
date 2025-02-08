import os

old_name = "C:\B4712\day6\sample.txt"
new_name = "C:\B4712\day6\example.txt"

os.rename(old_name, new_name)
print(f"File renamed from {old_name} to {new_name}")