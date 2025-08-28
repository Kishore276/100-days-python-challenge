def find_symmetric_pairs(arr):
    n = len(arr)
    mid = n // 2
    symmetric_pairs = []
    
    for i in range(mid):
        if arr[i] == arr[n - i - 1]:
            symmetric_pairs.append((arr[i], arr[n - i - 1]))
    
    return symmetric_pairs
arr = [1, 2, 3, 2, 1]
print(find_symmetric_pairs(arr))  