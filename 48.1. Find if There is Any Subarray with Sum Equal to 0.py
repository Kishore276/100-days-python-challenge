def has_zero_sum_subarray(arr):
    prefix_sum = set()
    current_sum = 0

    for num in arr:
        current_sum += num
        if current_sum == 0 or current_sum in prefix_sum:
            return True
        prefix_sum.add(current_sum)

    return False

arr = [3, 4, -7, 1, 5]
result = has_zero_sum_subarray(arr)
print("Has zero sum subarray:", result)