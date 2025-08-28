def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindromic(num):
    return str(num) == str(num)[::-1]

def count_palindromic_primes(N):
    count = 0
    for num in range(2, N):
        if is_prime(num) and is_palindromic(num):
            count += 1
    return count

N = int(input("Enter the value of N: "))
print(f"The number of palindromic primes below {N} is: {count_palindromic_primes(N)}")
