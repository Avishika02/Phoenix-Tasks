# Q1) Take the number (index of the option) as input from user and
# perform the corresponding drone's movement.
# Options: 1.Roll  2.Pitch  3.Yaw

# Take input from the user and convert it to an integer
# (input() always returns a string, so we must cast it to int for comparison)
choice = int(input("Enter movement type (1.Roll  2.Pitch  3.Yaw): "))

# Use if-elif-else to map the number to the correct drone action
if choice == 1:
    # Roll = drone tilts left/right, achieved by slowing down motors on one side
    print("Roll selected -> Slow down left motors for left roll OR right motors for right roll")
elif choice == 2:
    # Pitch = drone tilts forward/backward, achieved by speeding/slowing front-back motors
    print("Pitch selected -> Slow down front motors for forward pitch OR rear motors for backward pitch")
elif choice == 3:
    # Yaw = drone rotates about its vertical axis, achieved by changing diagonal motor speeds
    print("Yaw selected -> Speed up diagonal motor pair to rotate clockwise/counter-clockwise")
else:
    # Handle any invalid input outside 1-3
    print("Invalid choice! Please enter 1, 2, or 3.")