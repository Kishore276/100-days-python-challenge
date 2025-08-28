def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
def divisible_by_sum_of_digits(N):
    return [i for i in range(1, N + 1) if i % sum_of_digits(i) == 0]
N = 10
print(divisible_by_sum_of_digits(N))