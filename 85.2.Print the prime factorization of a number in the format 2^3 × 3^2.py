def prime_factorization(n):
    factors = {}
    while n % 2 == 0:
        if 2 in factors:
            factors[2] += 1
        else:
            factors[2] = 1
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
        factors[n] = 1
    factorization = ' x '.join(f"{key}^{value}" for key, value in factors.items())
    return factorization
number = 72
print(f"The prime factorization of {number} is: {prime_factorization(number)}")