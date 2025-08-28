def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        word = word.lower()
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency
sentence = "This is a test. This test is only a test."
print(word_frequency(sentence))