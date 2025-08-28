def diamond_pattern(n):
    # Print upper half
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    
    # Print lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

n = 5
diamond_pattern(n)