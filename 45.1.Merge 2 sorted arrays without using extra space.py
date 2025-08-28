def merge_sorted_arrays(arr1, arr2):
    # Calculate the length of both arrays
    m, n = len(arr1), len(arr2)
    
    i, j = m - 1, n - 1
    
    k = m + n - 1
   
    arr1 += [0] * n
    
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1
    
    # Copy remaining elements from arr2, if any
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1
    
    return arr1

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

arr1 = merge_sorted_arrays(arr1, arr2)
print(arr1)  