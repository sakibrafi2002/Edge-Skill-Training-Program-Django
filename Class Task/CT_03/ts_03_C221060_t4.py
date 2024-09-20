# Define a function to calculate the sum of all elements in the tuple
def sum_of_tuple_elements(t):
    total_sum = 0 #initialize a variable to store the total sum
    # Iterate through the tuple to calculate the sum
    for num in t: # initialize loop to calculate sum
        total_sum += num
    return total_sum # return the calculated sum

# Create a tuple of five elements
my_tuple = (5, 10, 15, 20, 25)

# Call the function and print the sum of the tuple elements
result = sum_of_tuple_elements(my_tuple)
print(f"Sum of all elements in the tuple: {result}") # print the result 

# Attempt to modify an element in the tuple (this will raise an error)
try:
    my_tuple[2] = 30  # Trying to modify the third element
except TypeError as e:
   print(f"Error: {e}")
