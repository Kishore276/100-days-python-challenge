def is_achilles_number(n):
    def prime_factors(n):
        factors = {}
        d = 2
        while d * d <= n:
            while (n % d) == 0:
                if d in factors:
                    factors[d] += 1
                else:
                    factors[d] = 1
                n //= d
            d += 1
        if n > 1:
            factors[n] = 1
        return factors
    factors = prime_factors(n)
    if not factors:
        return False
    powerful = all(exp >= 2 for exp in factors.values())
    perfect = sum(exp for exp in factors.values()) == 2
    return powerful and not perfect
n = 30
result = is_achilles_number(n)
print(result)