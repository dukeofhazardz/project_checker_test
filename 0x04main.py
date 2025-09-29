# Step 1: Create the student database
students = {
    "Alice": ["Math", "English", "Biology"],
    "Bob": ["History", "Physics"],
    "Charlie": ["Art", "Economics", "Math"]
}

# Step 2: Add a new course to Alice
students["Alice"].append("Computer Science")

# Step 3: Remove 'Art' from Charlie's courses
students["Charlie"].remove("Art")

# Step 4: Print all student names and their courses
for name, courses in students.items():
    print(f"Student: {name}")
    print("Courses:", ", ".join(courses))
    print("---")