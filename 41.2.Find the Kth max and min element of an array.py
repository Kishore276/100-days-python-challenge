import random

def quickselect(arr, k, max_element=True):
    if len(arr) == 1:
        return arr[0]

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]
    middle = [x for x in arr if x == pivot]
    right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]

    if max_element:
        if k <= len(right):
            return quickselect(right, k)
        elif k <= len(right) + len(middle):
            return middle[0]
        else:
            return quickselect(left, k - len(right) - len(middle))
    else:
        if k <= len(left):
            return quickselect(left, k)
        elif k <= len(left) + len(middle):
            return middle[0]
        else:
            return quickselect(right, k - len(left) - len(middle))

def find_kth_max_min(arr, k):
    max_element = quickselect(arr, k, max_element=True)
    min_element = quickselect(arr, k, max_element=False)
    return max_element, min_element

arr = [12, 3, 5, 7, 19]
k = 2
max_element, min_element = find_kth_max_min(arr, k)
print(f"Kth max element: {max_element}")
print(f"Kth min element: {min_element}")