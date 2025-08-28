import math
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    return int(math.log10(n)) + 1
number = 12345
print("Number of digits in {}: {}".format(number, count_digits(number))) 