def sort_012_array(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

arr = [1, 0, 2, 1, 0, 2, 1, 0, 2]
sorted_arr = sort_012_array(arr)
print(sorted_arr)