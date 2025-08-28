def replace_substring(s, old, new):
    return s.replace(old, new)

s = input("Enter a string: ")
old = input("Enter the sub-string to replace: ")
new = input("Enter the new sub-string: ")

new_string = replace_substring(s, old, new)
print("New string:", new_string)