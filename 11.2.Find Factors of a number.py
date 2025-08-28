def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# Ask the user for a number
number = int(input("Enter a number: "))

# Find and print the factors of the number
factors = find_factors(number)
print(f"Factors of {number} are: {factors}")
