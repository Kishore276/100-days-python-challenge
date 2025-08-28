my_array = [1, 2, 2, 3, 3, 3, 3, 4, 4, 4]
frequency = {}
for element in my_array:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1
sorted_array = sorted(frequency, key=frequency.get, reverse=True)
print(sorted_array) # [4, 3, 2, 1]