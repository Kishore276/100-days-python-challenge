def smallest_subarray_with_sum(arr, target_sum):
    n = len(arr)
    min_length = float('inf')
    current_sum = 0
    start = 0
    
    for end in range(n):
        current_sum += arr[end]
        
        while current_sum > target_sum:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1
            
    return min_length if min_length != float('inf') else 0
arr = [2, 1, 5, 2, 3, 2]
target_sum = 7
result = smallest_subarray_with_sum(arr, target_sum)
print(result)