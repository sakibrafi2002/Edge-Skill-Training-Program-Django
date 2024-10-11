# Define the function to compute sum, largest, smallest, and average using a loop
def operation_in_list(numbers):
    # Initialize variables
    total_sum = 0
    largest_number = numbers[0]  # Start by assuming the first element is the largest
    smallest_number = numbers[0]  # Start by assuming the first element is the smallest
    
    for number in numbers: # Loop through each number in the list
        total_sum += number # Add the number to the total sum
        if number > largest_number:  # Checks if the current number is larger than the largest number
            largest_number = number  # Update the largest number if the current number is greater
            
        if number < smallest_number: # Checks if current number is smaller than the smallest number
            smallest_number = number # Update the smallest number if the current number is smaller
    
    average = total_sum / len(numbers) # Calculating the average
    
    return total_sum, largest_number, smallest_number, average # returns all the calculated values

# Create a list of numbers
#numbers_list = [10, 25, 35, 42, 17, 89, 55]
numbers_list = [] #declare a list
total_number = int(input("Enter the amount of the numbers : ")) #takes input the number of the total numbers
for counter in range(0,total_number): # initialize loop for taking input
    number = int(input(f"Enter the {counter + 1} th number : ")) # takes the input
    numbers_list.append(number) # appends the number in the list

# Pass the list to the function
sum_of_numbers, largest_number, smallest_number, average_of_numbers = operation_in_list(numbers_list)

# Print the results of the operations
print(f"Sum of all numbers: {sum_of_numbers}") 
print(f"Largest number: {largest_number}")
print(f"Smallest number: {smallest_number}")
print(f"Average of numbers: {average_of_numbers}")
