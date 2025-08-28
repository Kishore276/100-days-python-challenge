def binary_to_octal(binary_value):
    try:
        # Convert binary to decimal
        decimal_value = int(binary_value, 2)
        # Convert decimal to octal
        octal_value = oct(decimal_value)[2:]  # Remove the '0o' prefix
        return octal_value
    except ValueError:
        return "Invalid binary number"
binary_value = "11111111"
octal_value = binary_to_octal(binary_value)
print(f"Binary {binary_value} to Octal is: {octal_value}")