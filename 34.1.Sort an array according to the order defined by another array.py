def sort_by_order(arr, order):
    # Step 1: Create a mapping of elements to their ranks
    rank_mapping = {x: i for i, x in enumerate(sorted(arr))}

    # Step 2: Sort arr according to the order defined by order
    sorted_arr = [x for _, x in sorted((rank_mapping[y], y) for y in order)]

    return sorted_arr

arr = [4, 2, 7, 1, 3]
order = [2, 1, 3, 4, 7]
result = sort_by_order(arr, order)
print(result)  