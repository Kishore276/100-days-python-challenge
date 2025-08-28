import heapq

def kth_smallest(matrix, k):
    min_heap = []
    for i in range(len(matrix)):
        heapq.heappush(min_heap, (matrix[i][0], i, 0))
    
    for _ in range(k):
        elem, row, col = heapq.heappop(min_heap)
        if col + 1 < len(matrix[row]):
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
    
    return elem

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 5
print(kth_smallest(matrix, k))  