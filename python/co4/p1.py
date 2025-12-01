class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        # Added parentheses for correct order of operations
        return 2 * (self.length + self.breadth)

# --- Driver Code ---

r1 = Rectangle(10, 5)
r2 = Rectangle(8, 8)

# Compare Areas
# r1 area = 50
# r2 area = 64

if r1.area() > r2.area():
    print("Rectangle 1 is larger")
elif r1.area() < r2.area():
    print("Rectangle 2 is large")
else:
    print("Both are Same")