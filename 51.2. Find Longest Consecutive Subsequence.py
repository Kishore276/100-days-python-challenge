def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only check for the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

nums = [100, 4, 200, 1, 3, 2]
result = longest_consecutive(nums)
print("Length of longest consecutive subsequence:", result)