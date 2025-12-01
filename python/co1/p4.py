
text = input("Enter a line of text: ")

words = text.lower().split()

unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

for word in unique_words:
    count = words.count(word)
    print(word, ":", count)
