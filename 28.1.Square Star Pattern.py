def print_square_star_pattern(n):
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()

n = 4
print_square_star_pattern(n)