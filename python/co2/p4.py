def pattern(r):
    for i in range(1, r+1):
        for j in range(1, i+1):
            print(i * j, end=" ")
        print() # Adds a newline after each row

r = int(input("Enter no of steps: "))
pattern(r)