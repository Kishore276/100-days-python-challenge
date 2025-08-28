def sum_of_divisors(n):
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  
                divisors_sum += n // i
    return divisors_sum
def abundant_numbers_below_n(N):
    abundant_numbers = []
    for i in range(12, N): 
        if sum_of_divisors(i) > i:
            abundant_numbers.append(i)
    return abundant_numbers
N = 100
print(f"Abundant numbers below {N}: {abundant_numbers_below_n(N)}")