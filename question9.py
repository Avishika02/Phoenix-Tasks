# Q9) Auto Return-to-Home System

drone_state = {
    "battery": 18,
    "altitude": 95,
    "signal_strength": 40,      # percent
    "distance_from_home": 850,  # metres
    "wind_speed": 38,           # km/h
    "obstacle_detected": True
}

# 1. Check ALL RTH trigger rules INDEPENDENTLY (using separate 'if' statements,
# NOT elif, because more than one condition can be true at the same time)
triggered = False  # flag to track if any rule fired, so we know when to print "all nominal"

if drone_state["battery"] < 20:
    print("CRITICAL: RTH triggered — Low Battery")
    triggered = True

if drone_state["signal_strength"] < 30:
    print("WARNING: RTH triggered — Signal Lost")
    triggered = True

if drone_state["wind_speed"] > 35:
    print("WARNING: RTH triggered — High Wind")
    triggered = True

if drone_state["obstacle_detected"] is True:
    print("CAUTION: Obstacle detected — Rerouting")
    triggered = True

if not triggered:
    print("All systems nominal")

# 2 & 3. While loop simulating descent from current altitude to 0 in steps of 15m,
# draining battery by 1% for every 15m descended, printing altitude + battery each step

current_altitude = drone_state["altitude"]
current_battery = drone_state["battery"]

print("\n--- Descent Simulation ---")
while current_altitude > 0:
    # Descend by 15m, but don't let altitude go negative
    current_altitude = max(0, current_altitude - 15)
    # Drain battery by 1% for this 15m step (don't let it go below 0)
    current_battery = max(0, current_battery - 1)
    print(f"Altitude: {current_altitude}m | Battery: {current_battery}%")
