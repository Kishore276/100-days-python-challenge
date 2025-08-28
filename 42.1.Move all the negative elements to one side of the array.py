def move_negative_elements(arr):
    left, right = 0, 0

    while right < len(arr):
        if arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right += 1
        else:
            right += 1

    return arr

arr = [-1, 2, -3, 4, 5, -6, 7, -8]
moved_arr = move_negative_elements(arr)
print(moved_arr)