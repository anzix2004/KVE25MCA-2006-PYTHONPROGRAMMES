
str1 = input("Enter String 1: ")
str2 = input("Enter String 2: ")

new_str1 = str2[0] + str1[1:]
new_str2 = str1[0] + str2[1:]

result = new_str1 + " " + new_str2
print(result)