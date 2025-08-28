def rearrange_alternate(arr):
    n = len(arr)
    pos_index = 0
    neg_index = 1

    # Separate positive and negative numbers
    while pos_index < n and neg_index < n:
        # Find the next positive number
        while pos_index < n and arr[pos_index] >= 0:
            pos_index += 2
        
        # Find the next negative number
        while neg_index < n and arr[neg_index] < 0:
            neg_index += 2
        
        # If there are still positive and negative numbers to swap
        if pos_index < n and neg_index < n:
            arr[pos_index], arr[neg_index] = arr[neg_index], arr[pos_index]

    return arr

arr = [1, -2, 3, -4, 5, -6, 7, -8]
result = rearrange_alternate(arr)
print("Rearranged array:", result)