def is_kaprekar(num):
    if num == 0:
        return False
    sq = str(num ** 2)
    d = len(str(num))
    left = int(sq[:-d]) if sq[:-d] else 0
    right = int(sq[-d:])
    return left + right == num
def kaprekar_numbers(N):
    return [i for i in range(1, N) if is_kaprekar(i)]
N = 100
result = kaprekar_numbers(N)
print(result)