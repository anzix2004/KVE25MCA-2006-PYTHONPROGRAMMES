char_list = []
word = input("Enter a word: ")

for i in word:
    # Check if character is a vowel
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        char_list.append(i)

print(char_list)