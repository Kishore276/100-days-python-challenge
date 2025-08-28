def are_disjoint(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return len(set1 & set2) == 0


arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(are_disjoint(arr1, arr2))  

arr1 = [1, 2, 3]
arr2 = [2, 4, 5]
print(are_disjoint(arr1, arr2))