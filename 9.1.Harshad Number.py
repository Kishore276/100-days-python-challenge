def is_harshad_number(number):
    digit_sum = sum(int(digit) for digit in str(number))
    return number % digit_sum == 0

# Example usage
number = int(input("Enter a number: "))
if is_harshad_number(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")
