import re
 
#Return a list containing every occurrence of "ai":
 
txt = "The rain in Spain"

x = re.findall("ai", txt)

print(x)


s = "GeeksforGeeks"

res = s.startswith("Geeks")

print(res)
 
 
 
txt = "Hello, welcome to my world"

x = txt.endswith("world")

print(x)


s = 'Readability counts.'
pattern = r'[aeoui]'
matches = re.finditer(pattern, s)
for match in matches:
    print(match)
 

 