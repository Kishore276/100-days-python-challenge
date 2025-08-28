def decimal_to_hexadecimal(decimal_value):
    try:
        decimal_value = int(decimal_value)
        hexadecimal_value = hex(decimal_value)[2:].upper()  # Remove the '0x' prefix and convert to uppercase
        return hexadecimal_value
    except ValueError:
        return "Invalid decimal number"
decimal_value = 255
hexadecimal_value = decimal_to_hexadecimal(decimal_value)
print(f"Decimal {decimal_value} to Hexadecimal is: {hexadecimal_value}")