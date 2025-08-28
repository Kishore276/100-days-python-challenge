def find_min_diff(arr, n, m):
    if m == 0 or n == 0:
        return 0
    # Sort the array
    arr.sort()
    if n < m:
        return -1
    min_diff = float('inf')
    
    for i in range(n - m + 1):
        current_diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, current_diff)
    
    return min_diff

arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7 
n = len(arr)
print(find_min_diff(arr, n, m)) 