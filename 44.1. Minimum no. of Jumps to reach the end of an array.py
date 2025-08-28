def min_jumps(arr):
    n = len(arr)
    jumps = [0] + [float('inf')] * (n - 1)

    for i in range(1, n):
        for j in range(i):
            if j + arr[j] >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)

    return jumps[-1]

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
min_jumps = min_jumps(arr)
print(min_jumps) 