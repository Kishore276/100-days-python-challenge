def is_abundant_number(number):
    divisor_sum = sum(i for i in range(1, number) if number % i == 0)
    
    return divisor_sum > number

number = int(input("Enter a number: "))
if is_abundant_number(number):
    print(f"{number} is an abundant number.")
else:
    print(f"{number} is not an abundant number.")
