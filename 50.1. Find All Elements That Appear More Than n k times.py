def find_majority_elements(arr, k):
    count_map = {}
    result = []

    for num in arr:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    threshold = len(arr) / k
    for num, count in count_map.items():
        if count > threshold:
            result.append(num)

    return result

arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
k = 3
result = find_majority_elements(arr, k)
print("Majority elements:", result)