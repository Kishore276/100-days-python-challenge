def print_sorted_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
    print()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_sorted_matrix(matrix)