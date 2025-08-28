def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_between(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

primes = prime_numbers_between(start, end)
print(f"Prime numbers between {start} and {end}: {primes}")
