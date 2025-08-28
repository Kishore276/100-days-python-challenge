def is_pronic_number(n):
    for i in range(int(n**0.5) + 1):
        if i * (i + 1) == n:
            return True
    return False
number = 6
print(is_pronic_number(number))  