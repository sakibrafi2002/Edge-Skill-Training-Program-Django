class Car:
    # Constructor to initialize the Car object with a model and fuel efficiency
    def __init__(self, model, fuel_efficiency):
        self.model = model  # Set the model of the car (e.g., "Toyota Corolla")
        self.fuel_efficiency = fuel_efficiency  # Set the fuel efficiency (e.g., km per liter)

    # Method to simulate driving the car
    def drive(self):
        print(f"{self.model} is being driven.")  # Print a message indicating the car is being driven

# Class to calculate fuel efficiency
class FuelEfficiencyCalculator:
    # Static method to calculate fuel efficiency
    def calculate_fuel_efficiency(miles, fuel):
        # Calculate fuel efficiency by dividing miles driven by fuel used
        return miles / fuel  # Return the calculated fuel efficiency (miles per gallon or km per liter)
