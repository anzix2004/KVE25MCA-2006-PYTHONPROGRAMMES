list1 = ["Anzil", "Hafis", "Arun"]
count = 0

for i in list1:
    for j in i:
        if j == 'A'or j == 'a':
            count += 1

print("Total 'a' found:", count)