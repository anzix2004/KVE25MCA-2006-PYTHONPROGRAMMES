def fact(n):
    print("factorial of ", n,"are :  ")
    for i in range (1,n+1):
        if n%i==0:
            print(i, end=" ")
fact(5)
