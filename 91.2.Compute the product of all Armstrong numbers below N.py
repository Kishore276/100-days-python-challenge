def is_armstrong(num):
    digits = list(map(int, str(num)))
    power = len(digits)
    return sum(d ** power for d in digits) == num

def product_of_armstrong_numbers(n):
    product = 1
    found = False
    for num in range(1, n):
        if is_armstrong(num):
            product *= num
            found = True
    return product if found else 0
N = int(input("Enter a number: "))
print("Product of Armstrong numbers below", N, "is:", product_of_armstrong_numbers(N))
