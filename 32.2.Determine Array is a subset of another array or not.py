def is_subset(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return set1.issubset(set2)

# Example usage:
arr1 = [1, 2, 3]
arr2 = [1, 2, 3, 4, 5]
print(is_subset(arr1, arr2))

arr1 = [1, 2, 3]
arr2 = [2, 4, 5]
print(is_subset(arr1, arr2)) 