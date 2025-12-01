def star_pattern(n):
    # Ascending part
    for i in range(1, n+1):
        print("*" * i)
    # Descending part
    for j in range(n-1, 0, -1):
        print("*" * j)

n = int(input("Enter no of rows: "))
star_pattern(n)