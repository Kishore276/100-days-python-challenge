def power(base, exponent):
    return base ** exponent

# Ask the user for the base and exponent
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Calculate and print the result
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
