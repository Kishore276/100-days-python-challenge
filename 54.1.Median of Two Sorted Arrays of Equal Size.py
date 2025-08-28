def find_median_sorted_arrays(arr1, arr2):
    n = len(arr1)
    if n != len(arr2):
        raise ValueError("Both arrays must be of equal size.")
    
    # Binary search on the smaller array
    if arr1[-1] < arr2[0]:
        return (arr1[n-1] + arr2[0]) / 2
    if arr2[-1] < arr1[0]:
        return (arr2[n-1] + arr1[0]) / 2

    low, high = 0, n
    while low <= high:
        partition1 = (low + high) // 2
        partition2 = n - partition1
        
        max_left1 = float('-inf') if partition1 == 0 else arr1[partition1 - 1]
        min_right1 = float('inf') if partition1 == n else arr1[partition1]
        
        max_left2 = float('-inf') if partition2 == 0 else arr2[partition2 - 1]
        min_right2 = float('inf') if partition2 == n else arr2[partition2]
        
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
        elif max_left1 > min_right2:
            high = partition1 - 1
        else:
            low = partition1 + 1
arr1 = [1, 3]
arr2 = [2, 4]
median = find_median_sorted_arrays(arr1, arr2)
print(median)  