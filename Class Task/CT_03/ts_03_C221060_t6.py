# Define a function to calculate average, highest, and lowest scores
def analyze_scores(scores_dict):
    scores = list(scores_dict.values()) # Get all scores from the dictionary
    average_score = sum(scores) / len(scores) # Calculate the average score
    highest_score = max(scores) # Find the highest score
    lowest_score = min(scores) # Find the lowest score
    
    return average_score, highest_score, lowest_score

# Create an empty dictionary to store student scores
student_scores = {}

# Take input from the user for the number of students
number_of_students = int(input("Enter the number of students: "))

# Loop to take student names and their scores as input
for _ in range(number_of_students):
    name = input("Enter student's name: ")
    score = int(input(f"Enter {name}'s score: "))
    # Add the name and score to the dictionary
    student_scores[name] = score

# Pass the dictionary to the function
average, highest, lowest = analyze_scores(student_scores)

# Print the results
print(f"\nAverage Score: {average}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
