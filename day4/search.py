import re
txt = "Hi hello planet"
#Check if the string starts with 'hello':
x = re.search("^Hi hello", txt)   # search method returns true if match , otherwise false
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


#exmp
txt = "hello planet"
#Check if the string starts with 'hello':
x = re.search("^hello", txt)   
# search method returns true if match , otherwise false
# ^ is used to match a string at the begining

if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

#exmp
txt = "Muruga doss"
#Check if the string if ends with doss :
# $ symbol is used to match at the end
x = re.search("doss$", txt)   
# search method returns true if match , otherwise false
if x:
  print("Yes, the string ends  doss")
else:
  print("No  ")

#exmp
txt = "welcome helo planet"
#Search for a sequence that starts with "he", followed by two (any) characters,
#and an "o":
x = re.search("he..o", txt)
if x:
   print("Match")
else:
   print("No match")    



txt = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.search("he.+o", txt)

if x:
   print("There is a match ")
else:
   print("There is no match  ")

#Zero or one occurrences

txt = "helo planet"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, 
# and an "o":
x = re.search("he.?o", txt)
if x:
   print("There is a match")
else:
   print("No Match  ")

