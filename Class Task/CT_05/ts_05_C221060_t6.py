class Bird:
    def fly(self):
        print("Flying...")

class Sparrow(Bird):
    pass  # Sparrow can fly

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")  # Violates LSP
