# Use list comprehension to create a list of even numbers from 1 to 50
even_numbers = [x for x in range(1, 51) if x % 2 == 0]

# Use a lambda function with map() to multiply each even number by 3
multiplied_by_3 = list(map(lambda x: x * 3, even_numbers))

# Print the original even numbers and the modified list
print(f"Even numbers from 1 to 50: {even_numbers}")
print(f"Even numbers multiplied by 3: {multiplied_by_3}")
