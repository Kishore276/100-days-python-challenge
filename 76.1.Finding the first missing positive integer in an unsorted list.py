def first_missing_positive(nums):
    nums = set(nums)
    i = 1
    while i in nums:
        i += 1
    return i
print(first_missing_positive([3, 4, -1, 1])) 