def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_cubes = sum(int(digit) ** num_digits for digit in num_str)
    return sum_cubes == n
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")