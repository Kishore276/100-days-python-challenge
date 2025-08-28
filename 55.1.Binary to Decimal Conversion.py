def binary_to_decimal(binary):
    decimal = 0
    binary = str(binary)
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal
binary_number = "1011"
print(f"The decimal value of binary {binary_number} is {binary_to_decimal(binary_number)}")