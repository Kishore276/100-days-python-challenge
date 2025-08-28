import math

def count_divisors(n):
    count = 0
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def smallest_number_with_divisors(d):
    num = 1
    while count_divisors(num) != d:
        num += 1
    return num

d = int(input("Enter the number of divisors: "))
print(f"The smallest number with {d} divisors is: {smallest_number_with_divisors(d)}")
