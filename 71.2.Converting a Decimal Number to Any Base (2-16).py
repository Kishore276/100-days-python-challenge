def convert_to_base(n, base):
    if n == 0:
        return "0"
    digits = ""
    while n > 0:
        remainder = n % base
        if remainder >= 10:
            digits += chr(remainder - 10 + ord('A'))
        else:
            digits += str(remainder)
        n //= base
    return digits[::-1]
number = 255
base = 16
print(convert_to_base(number, base))