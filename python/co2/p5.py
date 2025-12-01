def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

text = input("Enter a string: ")
print("Character frequency:", char_frequency(text))