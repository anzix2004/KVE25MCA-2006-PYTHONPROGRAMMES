class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    # This 'magic method' allows you to use the '<' symbol
    def __lt__(self, other):
        return self.area() < other.area()

# --- Driver Code ---

r1 = Rectangle(4, 6) # Area = 24
r2 = Rectangle(5, 5) # Area = 25

print(r1 < r2)