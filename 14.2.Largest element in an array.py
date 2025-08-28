def find_largest_element(arr):
    if not arr:
        return None
    largest = arr[0]
    for element in arr:
        if element > largest:
            largest = element
    return largest

# Ask the user for the array elements
array = list(map(int, input("Enter the array elements separated by spaces: ").split()))

# Find and print the largest element in the array
largest_element = find_largest_element(array)
print(f"The largest element in the array is: {largest_element}")
