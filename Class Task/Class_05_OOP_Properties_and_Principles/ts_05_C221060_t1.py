# Parent class "Vehicle" to represent general vehicles
class Vehicle:
    def __init__(self, model, year, wheels):
        # Initialize the common attributes for any vehicle
        self.model = model
        self.year = year
        self.wheels = wheels

    # Method to display general information about the vehicle
    def display_info(self):
        print(f"Model: {self.model}, Year: {self.year}, Wheels: {self.wheels}")


# Child class "Car" that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, model, year, wheels, doors):
        # Call the parent class constructor to initialize model, year, and wheels
        super().__init__(model, year, wheels)
        # Specific attribute for Car - number of doors
        self.doors = doors

    # Method to display car-specific information along with general vehicle info
    def display_info(self):
        # Call the parent class method to display common vehicle info
        super().display_info()
        # Print the specific information related to the Car (number of doors)
        print(f"Doors: {self.doors}")


# Child class "Bike" that inherits from Vehicle
class Bike(Vehicle):
    def __init__(self, model, year, wheels, cornering_angle):
        # Call the parent class constructor to initialize model, year, and wheels
        super().__init__(model, year, wheels)
        # Specific attribute for Bike - cornering angle
        self.cornering_angle = cornering_angle

    # Method to display bike-specific information along with general vehicle info
    def display_info(self):
        # Call the parent class method to display common vehicle info
        super().display_info()
        # Print the specific information related to the Bike (cornering angle)
        print(f"Cornering Angle: {self.cornering_angle} degrees")


# Create an instance of Car and test the methods
my_car = Car("Toyota Corolla", 2020, 4, 4)  # 4 doors for the car
print("Car Information:")  # Print a heading for clarity
my_car.display_info()  # Call the method to display the car's details

# Create an instance of Bike and test the methods
my_bike = Bike("Yamaha R15", 2021, 2, 30)  # Cornering angle is 30 degrees for the bike
print("\nBike Information:")  # Print a heading for clarity
my_bike.display_info()  # Call the method to display the bike's details
