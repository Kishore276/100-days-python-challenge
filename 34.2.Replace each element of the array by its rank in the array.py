def replace_with_ranks(arr):
    # Create a sorted copy of the array
    sorted_arr = sorted(arr)

    # Create a dictionary to map each element to its rank
    rank_mapping = {x: i for i, x in enumerate(sorted_arr)}

    # Replace each element with its rank
    ranked_arr = [rank_mapping[x] for x in arr]

    return ranked_arr

arr = [4, 2, 7, 1, 3]
result = replace_with_ranks(arr)
print(result) 