def hcf(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // hcf(x, y)

# Ask the user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find and print the LCM of the two numbers
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")
