# creating a class named person
class Person:
    # Constructor/Attributes to initialize name and age
    def __init__(self, name, age):
        self.name = name   # Set the 'name' attribute
        self.age = age     # Set the 'age' attribute

    # Method to display name and age
    def display_info(self):
        print(f"Name: {self.name}") # print the name
        print(f"Age: {self.age}") # print the age

    # Method to greet the person
    def greet(self):
        print(f"Hello, {self.name}! Nice to meet you.")

# Create an object of the Person class
person1 = Person("Rafi", 22)

# Display the name and age using the display_info method
person1.display_info()

# Greet the person using the greet method
person1.greet()
