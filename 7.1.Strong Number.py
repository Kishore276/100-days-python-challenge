import math

def is_strong_number(n):
    sum_factorials = sum(math.factorial(int(digit)) for digit in str(n))
    return sum_factorials == n
num = int(input("Enter a number: "))
if is_strong_number(num):
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is not a Strong Number.")