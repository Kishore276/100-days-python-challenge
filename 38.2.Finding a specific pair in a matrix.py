def find_pair(matrix, pair):
    for row in matrix:
        for elem in row:
            if elem == pair[0] and elem + 1 == pair[1]:
                return True
    return False

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pair = (2, 3)
print(find_pair(matrix, pair))  