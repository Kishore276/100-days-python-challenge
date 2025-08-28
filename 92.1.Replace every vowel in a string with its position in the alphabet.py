def replace_vowels_with_position(s):
    vowels = 'aeiouAEIOU'
    vowel_positions = {v: str(ord(v.lower()) - 96) for v in vowels}
    result = []

    for char in s:
        if char in vowel_positions:
            result.append(vowel_positions[char])
        else:
            result.append(char)

    return ''.join(result)

# Example usage
input_string = "Hello World"
print("Modified String:", replace_vowels_with_position(input_string))
