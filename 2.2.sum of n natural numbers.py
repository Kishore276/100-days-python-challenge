def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum
n = 5
result = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")