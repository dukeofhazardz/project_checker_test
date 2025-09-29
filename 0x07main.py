# Step 1: Set login and admin status
is_logged_in = True
is_admin = False

# Step 2: Check the conditions
if is_logged_in and is_admin:
    print("Welcome, Admin!")
elif is_logged_in and not is_admin:
    print("Welcome, User!")
else:
    print("Access Denied. Please log in.")