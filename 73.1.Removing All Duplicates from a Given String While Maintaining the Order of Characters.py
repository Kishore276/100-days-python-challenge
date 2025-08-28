def remove_duplicates(s):
    result = ""
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result
string = "abracadabra"
print(remove_duplicates(string))