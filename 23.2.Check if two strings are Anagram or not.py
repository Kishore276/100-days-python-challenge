def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if are_anagrams(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")