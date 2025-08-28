def octal_to_decimal(octal):
    try:
        decimal = 0
        octal = str(octal)
        for digit in octal:
            decimal = decimal * 8 + int(digit)
        return decimal
    except ValueError:
        return "Invalid octal number"
octal_number = "17"
result = octal_to_decimal(octal_number)
print(f"The decimal value of octal {octal_number} is {result}")
