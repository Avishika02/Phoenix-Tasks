# Q13) Take starting coordinates, move horizontally or vertically by N steps,
# printing each updated coordinate on every single-unit move.

# Try to input both coordinates together (comma-separated), as suggested
coords_input = input("Enter the starting x,y coordinates (comma-separated, e.g. 5,3): ")
x_str, y_str = coords_input.split(",")   # split on comma into two parts
x = int(x_str.strip())                   # strip() removes any accidental spaces
y = int(y_str.strip())

# Ask for movement direction
direction = input("Enter movement (horizontal or vertical): ").strip().lower()

# Ask for number of steps to move
steps = int(input("Enter the number of steps: "))

print("Movement path:")
output_points = []  # store all points to print them together at the end too

# Move one unit at a time, printing the updated coordinate after each single move
for step in range(1, steps + 1):
    if direction == "horizontal":
        x += 1          # each horizontal step increases x by 1
    elif direction == "vertical":
        y += 1           # each vertical step increases y by 1
    else:
        print("Invalid direction! Please enter 'horizontal' or 'vertical'.")
        break

    output_points.append((x, y))
    print(f"({x},{y})")  # print updated coordinate after this single move

# Final summary line showing the whole path together
print("\nFull path:", " ".join(f"({px},{py})" for px, py in output_points))
