def is_harshad_in_all_bases(n):
    for base in range(2, 11):
        digits = []
        temp = n
        while temp > 0:
            digits.append(temp % base)
            temp //= base
        digit_sum = sum(digits)
        if digit_sum == 0 or n % digit_sum != 0:
            return False
    return True
num = 18
print(f"{num} is a Harshad number in all bases 2–10: {is_harshad_in_all_bases(num)}")
