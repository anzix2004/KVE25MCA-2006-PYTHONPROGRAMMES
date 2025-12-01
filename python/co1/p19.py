# Program to find GCD
a = int(input("Enter first number: "))
b = int(input("Enter 2nd number: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

print("The GCD is ", a)