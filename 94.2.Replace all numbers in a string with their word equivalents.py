import re
digit_words = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three',
    '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
    '8': 'eight', '9': 'nine'
}
def number_to_words(match):
    return ' '.join(digit_words[d] for d in match.group())

def replace_numbers_with_words(text):
    return re.sub(r'\d+', number_to_words, text)

s = "I have 2 apples and 15 bananas."
print(replace_numbers_with_words(s))
