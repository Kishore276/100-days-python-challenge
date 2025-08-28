import math

def large_factorial(n):
    return math.gamma(n + 1)

n = 100
result = large_factorial(n)
print("Factorial of", n, ":", result)