# open close principle - open for extension , close for modification
# raise defines that each child of parent (Shape) must have the "area" method define,otherwise will show an error

# Base class 'Shape' that defines the method signature for calculating the area
class Shape:
    def area(self):
        # If a subclass does not override this method, an error will be raised
        raise NotImplementedError("Subclass must implement this method.")

# 'Circle' class inherits from 'Shape' and implements the 'area' method
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Initialize radius for Circle

    # Method to calculate the area of the Circle
    def area(self):
        return 3.14 * self.radius * self.radius  # π * radius^2

# 'Rectangle' class inherits from 'Shape' and implements the 'area' method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width   # Initialize width for Rectangle
        self.height = height # Initialize height for Rectangle

    # Method to calculate the area of the Rectangle
    def area(self):
        return self.width * self.height  # width * height

# Now you want to add a new shape of square , you can extend the shape
# New class 'Square' that inherits from 'Shape'
class Square(Shape):
    def __init__(self, side):
        self.side = side  # Initialize the side length for Square

    # Method to calculate the area of the Square
    def area(self):
        return self.side * self.side  # side * side

# Example usage for all shapes:

# Create an instance of Circle with radius 5
circle = Circle(5)
print(f"Area of Circle: {circle.area()}")  # Output: Area of Circle: 78.5

# Create an instance of Rectangle with width 4 and height 6
rectangle = Rectangle(4, 6)
print(f"Area of Rectangle: {rectangle.area()}")  # Output: Area of Rectangle: 24

# Create an instance of Square with side length 4
square = Square(4)
print(f"Area of Square: {square.area()}")  # Output: Area of Square: 16

# if you dont implement area() in child it will show an error as the parent method contains the template to raise an error if its not implemented