# Q6) Waypoint Mission Planner
# Tuples are used here because waypoint data should NOT change once set (immutability)

waypoints = (
    ("WP1", 23.0225, 72.5714, 50),
    ("WP2", 23.0312, 72.5801, 80),
    ("WP3", 23.0401, 72.5900, 100),
    ("WP4", 23.0225, 72.5714, 0),
)

# 1. Print the total number of waypoints
print("Total number of waypoints:", len(waypoints))

# 2. Use tuple unpacking to print each waypoint's details in a formatted line
print("\n--- Waypoint Details ---")
for name, lat, lon, alt in waypoints:   # unpack each tuple into 4 named variables directly
    print(f"{name}: Lat={lat}, Lon={lon}, Altitude={alt}m")

# 3. Find the waypoint with the highest altitude using a loop
highest_wp = waypoints[0]               # start by assuming the first waypoint is the highest
for wp in waypoints:
    if wp[3] > highest_wp[3]:           # index 3 is the altitude field
        highest_wp = wp                 # update if a higher one is found
print(f"\nWaypoint with highest altitude: {highest_wp[0]} at {highest_wp[3]}m")

# 4. Check if a specific waypoint tuple exists in waypoints
target = ("WP2", 23.0312, 72.5801, 80)
exists = target in waypoints            # 'in' operator checks membership for tuples too
print(f"\nDoes {target} exist in waypoints? {exists}")

# 5. Try to modify WP1's altitude to 60 -> tuples are immutable, this will raise TypeError
print("\nAttempting to modify WP1's altitude...")
try:
    waypoints[0][3] = 60   # this line will fail because tuples don't support item assignment
except TypeError:
    print("Waypoint data is immutable — mission integrity protected!")
