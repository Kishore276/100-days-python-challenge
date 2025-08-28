def rotate_string_left(s, n):
    n = n % len(s)
    return s[n:] + s[:n]
string = "abcdef"
n = 2
print(rotate_string_left(string, n))  