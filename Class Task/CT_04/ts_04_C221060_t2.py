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

    # Method to update the age attribute
    def update_age(self, new_age):
        self.age = new_age   # Update the 'age' attribute
        print(f"{self.name}'s age has been updated to {self.age}.")

# Create two objects of the Person class
person1 = Person("Rafi", 22)
person2 = Person("Sakib", 22)

# Display initial details of both persons
print("Initial Details: ")
person1.display_info()
print("") # prints a new line
person2.display_info()

# Update the age of person1
person1.update_age(26)
print("") # prints a new line

# Display updated details of both persons
print("\nUpdated Details:")
person1.display_info()
print("") # prints a new line
person2.display_info()
