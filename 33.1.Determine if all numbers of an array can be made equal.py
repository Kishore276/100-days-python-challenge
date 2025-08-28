def can_make_equal(arr):
    total_sum = sum(arr)
    length = len(arr)
    return total_sum % length == 0

arr = [2, 4, 6, 8]
print(can_make_equal(arr)) 