# Liskov substitution method ( SOLID --> L )
# It defines that the child class supports all method of the parent class

# But below, The parent Bird contains method named "fly", but the penguin type bird has an exception that it can't fly
# So penguins must not execute the "fly" method, It violates the Liskov substitution method.

# class Bird:
#     def fly(self):
#         print("Flying...")

# class Sparrow(Bird):
#     pass  # Sparrow can fly

# class Penguin(Bird):
#     def fly(self):
#         raise Exception("Penguins can't fly!")  # Violates LSP
    


# to make this better

# Bird parent class must not contain fly method as all the bird can not fly
class Bird:
    pass

# this FlyingBird class extends the capability of parent "Bird" by adding "fly" method,now this class can be inherited to the child bird class that can fly
class FlyingBird(Bird):
    def fly(self):
        print("Flying...")
class Sparrow(FlyingBird):
    pass  # Sparrow can fly

class Penguin(Bird):
    pass