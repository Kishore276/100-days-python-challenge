def string_length(s):
    count = 0
    for c in s:
        count += 1
    return count

s = input("Enter a string: ")
length = string_length(s)
print("Length of the string is", length)