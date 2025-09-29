# Step 1: Set the correct password
correct_password = "python123"

# Step 2: Prompt the user until they get it right
user_input = input("Enter the password: ")
while user_input != correct_password:
    print("Incorrect password. Try again.")
    user_input = input("Enter the password: ")

# Step 3: If correct, print access granted
print("Access granted.")