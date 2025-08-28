def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0 and is_prime(i):
            factors.append(i)
            n //= i
    return factors
def digit_sum(n):
    """Returns the sum of the digits of n."""
    return sum(int(digit) for digit in str(n))
def is_smith_number(n):
    if n < 2 or is_prime(n):
        return False  
    factors = prime_factors(n)
    if not factors:
        return False
    return digit_sum(n) == sum(digit_sum(factor) for factor in factors)
number = 4  
print(f"{number} is a Smith number: {is_smith_number(number)}")