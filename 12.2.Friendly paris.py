def sum_of_proper_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def find_friendly_pairs(limit):
    friendly_pairs = []
    for a in range(1, limit + 1):
        b = sum_of_proper_divisors(a)
        if a != b and a < b and sum_of_proper_divisors(b) == a:
            friendly_pairs.append((a, b))
    return friendly_pairs

limit = int(input("Enter the limit: "))

friendly_pairs = find_friendly_pairs(limit)
print(f"Friendly pairs up to {limit}: {friendly_pairs}")
