def triangle_star(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

triangle_star(4)