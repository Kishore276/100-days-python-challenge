def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_sphenic(n):
    count = 0
    product = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            count += 1
            product *= i
            if count > 3:
                return False
    return count == 3 and product <= n and n % product == 0

# Example usage
num = 30
if is_sphenic(num):
    print(f"{num} is a Sphenic number.")
else:
    print(f"{num} is NOT a Sphenic number.")
