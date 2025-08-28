def is_unhappy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n != 1
number = 2
print(is_unhappy_number(number)) 