def decimal_to_octal(decimal_value):
    try:
        decimal_value = int(decimal_value)
        octal_value = oct(decimal_value)[2:]  # Remove the '0o' prefix
        return octal_value
    except ValueError:
        return "Invalid decimal number"

decimal_value = 255
octal_value = decimal_to_octal(decimal_value)
print(f"Decimal {decimal_value} to Octal is: {octal_value}")