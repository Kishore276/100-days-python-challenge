def find_row_with_max_ones(matrix):
    max_count = 0
    max_row = -1
    
    for i in range(len(matrix)):
        count = matrix[i].count(1)
        
        if count > max_count:
            max_count = count
            max_row = i
    
    return max_row

matrix = [
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 1]
]

row_index = find_row_with_max_ones(matrix)
print("Row index with maximum number of 1's:", row_index)