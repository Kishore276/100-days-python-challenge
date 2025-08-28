import math

def replace_digit_with_factorial(num):
    num_str = str(num)
    result = []

    for char in num_str:
        if char.isdigit():
            factorial = str(math.factorial(int(char)))
            result.append(factorial)
        else:
            result.append(char)

    return ''.join(result)
number = int(input("Enter a number: "))
print("Modified Number:", replace_digit_with_factorial(number))
