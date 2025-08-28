def hcf(x, y):
    while y:
        x, y = y, x % y
    return x

# Ask the user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find and print the HCF of the two numbers
result = hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is: {result}")
