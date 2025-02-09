def reverse_number(n):
    return int(str(n)[::-1])

def is_adam_number(num):
    square_num = num ** 2
    reversed_num = reverse_number(num)
    square_reversed_num = reversed_num ** 2
    reversed_square_num = reverse_number(square_num)
    return square_reversed_num == reversed_square_num

num = int(input("Enter a number: "))

if is_adam_number(num):
    print(f"{num} is an Adam Number")
else:
    print(f"{num} is NOT an Adam Number")