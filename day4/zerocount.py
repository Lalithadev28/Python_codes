def count_zeros(n):
    return str(n).count('0')
num = int(input("Enter a number: "))
zero_count = count_zeros(num)

print("Number of zeros in given num: ",zero_count)
    