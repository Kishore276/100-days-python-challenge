def min_sum_absolute_difference(arr):
    arr.sort()
    n = len(arr)
    if n % 2 != 0:
        median = arr[n // 2]
    else:
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2
    return sum(abs(x - median) for x in arr)

arr = [1, 3, 5, 7, 9]
print(min_sum_absolute_difference(arr))  