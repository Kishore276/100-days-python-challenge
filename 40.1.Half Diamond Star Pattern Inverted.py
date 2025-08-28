def half_diamond_inverted(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

n = 5
half_diamond_inverted(n)