x = int(input("Enter the start year: "))
y = int(input("Enter the final year: "))
leap_years = []

while x <= y:
    # A leap year is divisible by 4 AND (not divisible by 100 OR divisible by 400)
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        leap_years.append(x)
    x += 1

print("Future leap years are:", leap_years)