def is_zuckerman_number(n):
    digits = [int(d) for d in str(n)]
    product = 1
    for d in digits:
        product *= d
    if product == 0:
        return False

    return n % product == 0
num = 100
print(f"{num} is a Zuckerman number: {is_zuckerman_number(num)}")
