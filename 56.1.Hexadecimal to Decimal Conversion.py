def hex_to_decimal(hex_value):
    try:
        decimal_value = int(hex_value, 16)
        return decimal_value
    except ValueError:
        return "Invalid hexadecimal number"
hex_value = "1A3F"
decimal_value = hex_to_decimal(hex_value)
print(f"Hexadecimal {hex_value} to Decimal is: {decimal_value}")