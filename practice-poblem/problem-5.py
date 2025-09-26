def most_frequent_word(text):
    words = text.split()
    freq = {}

    # count frequencies
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # find word with maximum frequency
    max_word = max(freq, key=freq.get)
    return f"{max_word} -> {freq[max_word]}"

# Example usage
s = "hello how are you i am fine thank you"
print(most_frequent_word(s))
