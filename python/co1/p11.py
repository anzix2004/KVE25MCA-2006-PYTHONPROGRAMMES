a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "is biggest number")
elif b >= a and b >= c:
    print(b, "is biggest number")
else:
    print(c, "is biggest number")
