my_array = [1, 2, 2, 3, 3, 3, 4]
repeating_elements = [element for element in set(my_array) if my_array.count(element) > 1]
print(repeating_elements) 