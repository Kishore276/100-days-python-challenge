def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def can_be_expressed_as_sum_of_two_primes(n):
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            return True
    return False
number_to_check = 10
result = can_be_expressed_as_sum_of_two_primes(number_to_check)
print(f"The number {number_to_check} can be expressed as a sum of two prime numbers: {result}")