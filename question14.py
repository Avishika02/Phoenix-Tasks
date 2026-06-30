# Q14) Take user id and password, convert to lowercase, compare with
# predefined credentials, print success message if matched

# Predefined (correct) credentials -- already stored in lowercase for fair comparison
correct_user_id = "px4admin"
correct_password = "skyfall123"

# Take input from the user
entered_user_id = input("Enter user ID: ")
entered_password = input("Enter password: ")

# Convert both entered values to lowercase before comparing
# (so that "PX4Admin" and "px4admin" are treated as the same)
entered_user_id_lower = entered_user_id.lower()
entered_password_lower = entered_password.lower()

# Compare with the predefined credentials
if entered_user_id_lower == correct_user_id and entered_password_lower == correct_password:
    print("Drone connected successfully")
else:
    print("Connection failed: Invalid user ID or password")
