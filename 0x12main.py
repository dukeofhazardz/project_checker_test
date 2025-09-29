# Student Grading System
# Accepts multiple student names and scores, assigns letter grades,
# and generates a final report.

print("Student Grading System")

# Dictionary to store student data {name: (score, grade)}
students = {}

while True:
    # Get student name
    name = input("Enter student name (or type 'done' to finish): ")
    
    if name.lower() == "done":
        break  # exit loop when user is finished
    
    # Get score
    score = int(input(f"Enter {name}'s score: "))
    
    # Assign grade based on score
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    # Store in dictionary
    students[name] = (score, grade)
    print()  # blank line for readability

# Final Report
print("--- Final Report ---")
for name, (score, grade) in students.items():
    print(f"{name}: {score} - Grade {grade}")