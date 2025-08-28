def find_union_intersection(arr1, arr2):
    union = []
    intersection = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if arr1[i] not in union:
                union.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            if arr2[j] not in union:
                union.append(arr2[j])
            j += 1
        else:
            if arr1[i] not in union:
                union.append(arr1[i])
            if arr1[i] not in intersection:
                intersection.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if arr1[i] not in union:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):
        if arr2[j] not in union:
            union.append(arr2[j])
        j += 1

    return union, intersection

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
union, intersection = find_union_intersection(arr1, arr2)
print("Union:", union)
print("Intersection:", intersection) 