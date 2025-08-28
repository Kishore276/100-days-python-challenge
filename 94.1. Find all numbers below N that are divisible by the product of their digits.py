def product_of_digits(n):
    product = 1
    for digit in str(n):
        if digit == '0':
            return 0 
        product *= int(digit)
    return product

def find_divisible_numbers(N):
    result = []
    for num in range(1, N):
        prod = product_of_digits(num)
        if prod != 0 and num % prod == 0:
            result.append(num)
    return result
N = 100
print(find_divisible_numbers(N))
