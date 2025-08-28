def common_elements(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    common = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            common.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return common

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 5, 7]
arr3 = [1, 2, 3, 4, 5]
result = common_elements(arr1, arr2, arr3)
print("Common elements:", result)