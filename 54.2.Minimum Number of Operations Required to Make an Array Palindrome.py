def min_operations_to_palindrome(arr):
    n = len(arr)
    operations = 0
    
    left, right = 0, n - 1
    while left < right:
        if arr[left] != arr[right]:
            operations += 1
        left += 1
        right -= 1
        
    return operations
arr = [1, 2, 3, 4, 3, 2, 1]
result = min_operations_to_palindrome(arr)
print(result) 

arr2 = [1, 2, 3, 4]
result2 = min_operations_to_palindrome(arr2)
print(result2) 