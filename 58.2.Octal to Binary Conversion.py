def octal_to_binary(octal_value):
    try:
        # Convert octal to decimal
        decimal_value = int(octal_value, 8)
        # Convert decimal to binary
        binary_value = bin(decimal_value)[2:]  # Remove the '0b' prefix
        return binary_value
    except ValueError:
        return "Invalid octal number"
octal_value = "377"
binary_value = octal_to_binary(octal_value)
print(f"Octal {octal_value} to Binary is: {binary_value}")