def is_perfect(n):
    divisors_sum = 1  # start with 1 (every number is divisible by 1)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n and n != 1

def print_perfect_numbers_below(N):
    print(f"Perfect numbers below {N}:")
    for i in range(2, N):
        if is_perfect(i):
            print(i, end=' ')
N = 10000
print_perfect_numbers_below(N)
