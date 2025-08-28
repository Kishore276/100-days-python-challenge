def replace_spaces_with_previous_char(s):
    result = []
    for i in range(len(s)):
        if s[i] == ' ' and i > 0:
            prev_char = chr(ord(s[i - 1]) - 1) 
            result.append(prev_char)
        else:
            result.append(s[i])
    return ''.join(result)
input_string = "Hello World"
print("Modified String:", replace_spaces_with_previous_char(input_string))
