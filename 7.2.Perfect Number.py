def is_perfect_number(n):
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n
num = int(input("Enter a number: "))
if is_perfect_number(num):
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")