def reverse_number(n):
    sign = -1 if n < 0 else 1
    n *= sign
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return sign * reversed_num
num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print(f"The reverse of {num} is: {reversed_num}")