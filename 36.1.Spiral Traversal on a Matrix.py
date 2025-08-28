def spiral_traversal(matrix):
    result = []
    while matrix:
        # Extract the first row
        result += matrix.pop(0)
        if matrix and matrix[0]:
            # Rotate the matrix clockwise
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            # Rotate the matrix clockwise
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
result = spiral_traversal(matrix)
print(result) 