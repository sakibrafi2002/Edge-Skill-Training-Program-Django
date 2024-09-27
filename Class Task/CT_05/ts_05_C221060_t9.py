# Function to perform division with error handling
def divide_numbers():
    try:
        # Prompt the user for two numbers
        num1 = float(input("Enter the first number: "))  # Convert input to float
        num2 = float(input("Enter the second number: "))  # Convert input to float

        # Perform division
        result = num1 / num2

    # Handle division by zero error
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    
    # Handle invalid input error (e.g., non-numeric input)
    except ValueError:
        print("Error: Please enter valid numbers.")
    
    # If no errors, display the result
    else:
        print(f"Result: {num1} divided by {num2} is {result}")

# Call the function to run the program
divide_numbers()
