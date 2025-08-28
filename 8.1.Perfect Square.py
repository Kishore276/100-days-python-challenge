import math

def is_perfect_square(n):
    sqrt = math.sqrt(n)
    return sqrt == int(sqrt)

num = int(input("Enter a number: "))
if is_perfect_square(num):
    print(f"{num} is a Perfect Square.")
else:
    print(f"{num} is not a Perfect Square.")