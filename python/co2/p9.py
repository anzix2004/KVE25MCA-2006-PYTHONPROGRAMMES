def long_word(words):
    long = max(words, key=len)
    return len(long)

words = input("Enter words separated by space: ").split()
print("Length of longest word:", long_word(words))