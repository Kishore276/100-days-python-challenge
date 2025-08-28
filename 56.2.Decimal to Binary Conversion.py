def decimal_to_binary(decimal_value):
    try:
        # Ensure the input is an integer
        decimal_value = int(decimal_value)
        binary_value = bin(decimal_value)[2:]  # Remove the '0b' prefix
        return binary_value
    except ValueError:
        return "Invalid decimal number"
decimal_value = 255
binary_value = decimal_to_binary(decimal_value)
print(f"Decimal {decimal_value} to Binary is: {binary_value}")