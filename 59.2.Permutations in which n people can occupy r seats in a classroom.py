import math

def permutations(n, r):
    if r > n:
        return "r cannot be greater than n"
    return math.factorial(n) // math.factorial(n - r)
n = 5  # Total people
r = 3  # Seats to fill
perm = permutations(n, r)
print(f"The number of permutations of {n} people occupying {r} seats is: {perm}")