def count_digit_occurrences(input_value, digit):
    input_str = str(input_value)
    digit_str = str(digit)
    return input_str.count(digit_str)
input_value = 1234567890123456789
digit = 3
print("The digit {} occurs {} times in the input value {}.".format(digit, count_digit_occurrences(input_value, digit), input_value)) 