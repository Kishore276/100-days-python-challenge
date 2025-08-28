def product_of_odd_position_digits(number):
    number_str = str(number)
    product = 1
    found = False
    for i in range(0, len(number_str), 2):  # 0-based index, so 0,2,4... are odd positions (1-based)
        digit = int(number_str[i])
        product *= digit
        found = True
    return product if found else 0
num = 123456
result = product_of_odd_position_digits(num)
print(f"Product of odd-positioned digits in {num} is {result}")
