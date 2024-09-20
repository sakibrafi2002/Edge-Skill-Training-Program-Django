# Define a function to find intersection and difference between two sets
def analyze_students(set1, set2):
    students_in_both = set1.intersection(set2) # Find the intersection (students in both sets)
    
    students_only_in_one = set1.symmetric_difference(set2) # Find the difference (students only in one of the sets)
    
    return students_in_both, students_only_in_one # return the values

# Create two sets of student names
students_set1 = {"Rayhan", "Rafi", "Mamun", "Mutasim", "Nahian"}
students_set2 = {"Rafi", "Nahian", "Fahim", "Hasan", "Mamun"}

# Pass the sets to the function
students_in_both, students_only_in_one = analyze_students(students_set1, students_set2)

# Print the results
print(f"Students in both sets (intersection): {students_in_both}")
print(f"Students only in one set (difference): {students_only_in_one}")
