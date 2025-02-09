'''str1 = Emma-is-a-data-scientist

Expected Output:

Displaying each substring

Emma
is
a
data
scientist '''

str1 = "Emma-is-a-data-scientist"
substrings = str1.split('-')
for substring in substrings:
    print(substring)

