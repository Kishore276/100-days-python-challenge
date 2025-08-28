def digit_to_word(digit):
    digit_to_word_map = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    return digit_to_word_map[digit]

def number_to_words(number):
    if number < 0:
        return 'minus ' + number_to_words(-number)
    elif number < 10:
        return digit_to_word(number)
    elif number < 20:
        return {
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
        }[number]
    elif number < 100:
        tens = {
            2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
            6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
        }
        if number % 10 == 0:
            return tens[number // 10]
        else:
            return tens[number // 10] + '-' + digit_to_word(number % 10)
    elif number < 1000:
        if number % 100 == 0:
            return digit_to_word(number // 100) + ' hundred'
        else:
            return digit_to_word(number // 100) + ' hundred and ' + number_to_words(number % 100)
number = 123
print("Number {} in words: {}".format(number, number_to_words(number)))  # Output: one hundred and twenty-three