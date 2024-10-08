# Interface segregation (ISP) ( SOLID -> I)

# In vehicles, some are drivable and some are flyable, with a note that some are both.
# It is not logical for drive and fly to be contained in the same parent class, as shown in the following code.

# Not recommended

class Vehicle:
    def drive(self):
        pass

    def fly(self):
        pass

# Car class inherits from Vehicle, but cars can't fly.
class Car(Vehicle):
    def drive(self):
        # Cars can drive, so this works fine.
        print("Driving on the road.")

    def fly(self):
        # Cars can't fly, so we raise an error.
        raise NotImplementedError("Cars can't fly.")

# Airplane class inherits from Vehicle, but airplanes can't drive.
class Airplane(Vehicle):
    def fly(self):
        # Airplanes can fly, so this works fine.
        print("Flying in the sky.")

    def drive(self):
        # Airplanes can't drive, so we raise an error.
        raise NotImplementedError("Airplanes can't drive.")


# Better approach: Use separate classes for Drivable and Flyable
# Some vehicles can drive, and others can fly.
# This is the Interface Segregation Principle (ISP) from SOLID, meaning separate interfaces for separate behaviors.

# Drivable class is for vehicles that can drive.
class Drivable:
    def drive(self):
        pass

# Flyable class is for vehicles that can fly.
class Flyable:
    def fly(self):
        pass

# Car class inherits from Drivable, because it can only drive.
class Car(Drivable):
    def drive(self):
        # Cars can drive, so this works fine.
        print("Driving on the road.")

# Airplane class inherits from Flyable, because it can only fly.
class Airplane(Flyable):
    def fly(self):
        # Airplanes can fly, so this works fine.
        print("Flying in the sky.")
