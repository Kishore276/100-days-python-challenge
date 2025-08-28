from sympy import primerange
from itertools import product

def count_divisors(n):
    """Returns the number of divisors of n."""
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def find_integers_with_exactly_x_divisors(x, limit=10000):
    """Finds integers with exactly x divisors up to a given limit."""
    primes = list(primerange(1, 100))  
    results = set()
    for e1 in range(x):  # e1 + 1
        for e2 in range(x):  # e2 + 1
            if (e1 + 1) * (e2 + 1) == x:
                n = (primes[0] ** e1) * (primes[1] ** e2)
                if n <= limit:
                    results.add(n)

    return sorted(results)
x = 6
integers_with_x_divisors = find_integers_with_exactly_x_divisors(x)
print(f"Integers with exactly {x} divisors: {integers_with_x_divisors}")