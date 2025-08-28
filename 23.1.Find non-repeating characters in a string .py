def non_repeating_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    non_repeating = [char for char, count in char_count.items() if count == 1]
    return non_repeating

s = input("Enter a string: ")
non_repeating = non_repeating_chars(s)
print("Non-repeating characters:", non_repeating)