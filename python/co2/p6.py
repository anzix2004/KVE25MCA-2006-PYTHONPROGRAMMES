def add_ing(s):
    if s.endswith("ing"):
        return s + "ly"
    else:
        return s + "ing"

word = input("Enter a String: ")
print("Modified String:", add_ing(word))