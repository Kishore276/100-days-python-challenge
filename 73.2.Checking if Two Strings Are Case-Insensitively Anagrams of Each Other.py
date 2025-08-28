def are_anagrams(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return sorted(s1) == sorted(s2)
string1 = "Listen"
string2 = "Silent"
print(are_anagrams(string1, string2))