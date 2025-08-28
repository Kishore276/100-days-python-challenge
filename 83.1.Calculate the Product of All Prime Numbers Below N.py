def product_of_primes_below_n(n):
    """Calculate the product of all prime numbers below n."""
    if n < 2:
        return 1  # No primes below 2

    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    product = 1
    for number in range(2, n):
        if is_prime(number):
            product *= number

    return product
N = 10
print(f"Product of all prime numbers below {N}: {product_of_primes_below_n(N)}")