def three_way_partition(arr, low_val, high_val):
    n = len(arr)
    low = 0
    mid = 0
    high = n - 1
    
    while mid <= high:
        if arr[mid] < low_val:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] > high_val:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1
            
    return arr
arr = [3, 5, 2, 1, 4, 9, 7, 6]
low_val = 3
high_val = 6
result = three_way_partition(arr, low_val, high_val)
print(result)  