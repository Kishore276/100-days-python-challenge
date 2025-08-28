def max_subarray_sum(arr):
    max_sum = float('-inf')
    curr_sum = 0

    for num in arr:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
max_sum = max_subarray_sum(arr)
print(max_sum)  