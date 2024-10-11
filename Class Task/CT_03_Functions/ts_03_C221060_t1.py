# Define a function to calculate the factorial of a number
def factorial(n):
    if n == 0: # If the number is 0, return 1 (since factorial of 0 is 1)
        return 1
    else:
        return n * factorial(n-1) # Here n is multiplied by the factorial of (n-1) recursively

# Ask the user to enter a number and convert it to an integer
value = int(input("Enter a Number : "))

# Call the factorial function with the user input and store the result in 'ans' variable
ans = factorial(value)

# Print the result (factorial of the number) in a clear format
print("The factorial of the number", value, "is:", ans)
