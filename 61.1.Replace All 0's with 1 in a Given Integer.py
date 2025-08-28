def replace_zeros_with_ones(n):
    return int(str(n).replace('0', '1'))
number = 105040
result = replace_zeros_with_ones(number)
print(f"Replacing 0's with 1's in {number} gives: {result}")