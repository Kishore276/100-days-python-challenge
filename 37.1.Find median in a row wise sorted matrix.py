def find_median(matrix):
    total_count = len(matrix) * len(matrix[0])
    mid = total_count // 2
    
    row = 0
    col = 0
    count = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count += 1
            
            if count == mid + 1:
                row = i
                col = j
                
    if total_count % 2 != 0:
        return matrix[row][col]
    else:
        next_row = row
        next_col = col + 1
        
        if next_col == len(matrix[0]):
            next_row += 1
            next_col = 0
        
        return (matrix[row][col] + matrix[next_row][next_col]) / 2

matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]

median = find_median(matrix)
print("Median:", median)