# Q4) Drone Telemetry Log Parser
# Parse a pipe-separated telemetry string and extract individual fields

telemetry = "DRONE_ID:PX4_001|ALT:120.5m|SPEED:18.3kmph|BATT:67%|STATUS:HOVERING|GPS:23.0225N,72.5714E"

# 1. Split the telemetry string by "|" to get individual key:value segments
segments = telemetry.split("|")
# segments -> ['DRONE_ID:PX4_001', 'ALT:120.5m', 'SPEED:18.3kmph', 'BATT:67%', 'STATUS:HOVERING', 'GPS:23.0225N,72.5714E']

# Each segment has format "KEY:VALUE", so split each on the first ":"
drone_id = segments[0].split(":")[1]                       # "PX4_001"

# ALT:120.5m -> remove the trailing "m" using rstrip, then convert to float
altitude = float(segments[1].split(":")[1].rstrip("m"))    # 120.5

# SPEED:18.3kmph -> remove "kmph" suffix, then convert to float
speed = float(segments[2].split(":")[1].rstrip("kmph"))    # 18.3

# BATT:67% -> remove "%" suffix, then convert to int
battery = int(segments[3].split(":")[1].rstrip("%"))       # 67

# STATUS:HOVERING -> just take the value as-is
status = segments[4].split(":")[1]                         # "HOVERING"

# GPS:23.0225N,72.5714E -> take everything after "GPS:"
gps_coords = segments[5].split(":", 1)[1]                  # "23.0225N,72.5714E"

print("Drone ID:", drone_id)
print("Altitude:", altitude, "(type:", type(altitude), ")")
print("Speed:", speed, "(type:", type(speed), ")")
print("Battery:", battery, "(type:", type(battery), ")")
print("GPS Coordinates:", gps_coords)

# 2. Check if status contains "HOVER" (case-insensitive)
is_hovering = "hover" in status.lower()   # convert both to lowercase before checking substring
print("\nIs the drone hovering?", is_hovering)

# 3. Replace "HOVERING" with "RETURNING_HOME" in the original telemetry string
updated_telemetry = telemetry.replace("HOVERING", "RETURNING_HOME")
print("Updated telemetry string:", updated_telemetry)

# 4. Print a formatted summary using f-strings
print(f"\n[{drone_id}] Alt: {altitude}m | Batt: {battery}% | Coords: {gps_coords}")
