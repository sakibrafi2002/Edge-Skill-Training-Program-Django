# Import the custom_module_1 module
# from Modules/custom_module_1 import 
from Modules  import custom_module_1
# Input for Celsius to Fahrenheit conversion
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = custom_module_1.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")

# Input for calculating the area of a circle
radius = float(input("Enter the radius of the circle: "))
area = custom_module_1.area_of_circle(radius)
print(f"The area of the circle with radius {radius} is: {area}")

print(type([]))