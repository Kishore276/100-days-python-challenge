def parallelogram_star_pattern(rows, columns):
    for i in range(rows):
        print(" " * i, end="")
        for j in range(columns):
            print("*", end=" ")
        print()

rows = 4
columns = 8
parallelogram_star_pattern(rows, columns)