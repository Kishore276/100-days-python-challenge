def minimize_max_diff(arr, k):
    arr.sort()
    n = len(arr)
    low, high = 0, n - 1
    res = float('inf')

    while low < high:
        mid = (low + high) // 2
        if can_split(arr, mid, k):
            res = min(res, arr[mid] - arr[0])
            high = mid - 1
        else:
            low = mid + 1

    return res

def can_split(arr, mid, k):
    cnt = 1
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - prev > mid:
            cnt += 1
            prev = arr[i]
    return cnt <= k

arr = [2, 6, 3, 4, 7, 2, 10, 3, 2, 9]
k = 4
min_max_diff = minimize_max_diff(arr, k)
print(min_max_diff) 