def max_product_subarray(arr):
    n = len(arr)
    max_product = [0] * n
    min_product = [0] * n
    max_product[0] = min_product[0] = result = arr[0]
    
    for i in range(1, n):
        if arr[i] < 0:
            max_product[i], min_product[i] = min_product[i-1], max_product[i-1]
        else:
            max_product[i], min_product[i] = max_product[i-1], min_product[i-1]
        
        max_product[i] = max(arr[i], max_product[i] * arr[i])
        min_product[i] = min(arr[i], min_product[i] * arr[i])
        
        result = max(result, max_product[i])
    
    return result
arr = [2, 3, -2, 4]
print(max_product_subarray(arr))