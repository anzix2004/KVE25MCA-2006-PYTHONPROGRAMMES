list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# Check Lengths
result1 = len(list1)
result2 = len(list2)

if result1 == result2:
    print("Lists are of Same length")
else:
    print("Length not Same")

# Check Sums
result3 = sum(list1)
result4 = sum(list2)

if result3 == result4:
    print("Sum is Same")
else:
    print("Sum is different")

# Check Common Elements
found_common = False
i = 0
while i < len(list1):
    j = 0
    while j < len(list2):
        if list1[i] == list2[j]:
            found_common = True
        j += 1
    i += 1

if found_common:
    print("Lists have Common values")
else:
    print("No Common values found")