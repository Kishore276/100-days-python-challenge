def print_triangular_numbers_below(N):
    triangular_numbers = []
    n = 1
    while True:
        t = n * (n + 1) // 2
        if t >= N:
            break
        triangular_numbers.append(t)
        n += 1
    print("Triangular numbers below", N, ":", triangular_numbers)
print_triangular_numbers_below(50)
