import math
from functools import reduce
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
def smallest_multiple(N):
    return reduce(lcm, range(1, N + 1))
N = 10
print(smallest_multiple(N))