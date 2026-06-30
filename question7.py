# Q7) Fleet Health Monitor
# Dictionary of dictionaries: outer key = drone ID, inner dict = drone's stats

fleet = {
    "PX4_001": {"battery": 87, "altitude": 120, "status": "active", "payload_kg": 1.2},
    "PX4_002": {"battery": 23, "altitude": 0, "status": "grounded", "payload_kg": 0},
    "PX4_003": {"battery": 56, "altitude": 85, "status": "active", "payload_kg": 0.8},
    "PX4_004": {"battery": 11, "altitude": 30, "status": "returning", "payload_kg": 0.5},
}

# 1. Add "PX4_005" with the given stats
fleet["PX4_005"] = {"battery": 95, "altitude": 0, "status": "standby", "payload_kg": 0}
print("PX4_005 added to fleet.")

# 2. Remove "PX4_002" using .pop() and print its details before removal
removed_drone = fleet.pop("PX4_002")   # .pop() removes the key AND returns its value
print("Removed PX4_002. Its details were:", removed_drone)

# 3. Print all active drones and their battery levels
print("\n--- Active Drones ---")
for drone_id, info in fleet.items():            # .items() gives (key, value) pairs
    if info["status"] == "active":
        print(f"{drone_id}: Battery = {info['battery']}%")

# 4. Find the drone with the lowest battery among drones currently in the air (altitude > 0)
airborne_drones = {k: v for k, v in fleet.items() if v["altitude"] > 0}  # dict comprehension filter
lowest_battery_drone = min(airborne_drones, key=lambda d: airborne_drones[d]["battery"])
print(f"\nAirborne drone with lowest battery: {lowest_battery_drone} "
      f"({airborne_drones[lowest_battery_drone]['battery']}%)")

# 5. Update every drone with battery < 30 to status = "critical_low_battery"
for drone_id, info in fleet.items():
    if info["battery"] < 30:
        info["status"] = "critical_low_battery"  # modifying dict value in place

# 6. Print a final formatted fleet summary
print("\n--- Final Fleet Summary ---")
for drone_id, info in fleet.items():
    print(f"{drone_id} | Battery: {info['battery']}% | Altitude: {info['altitude']}m | "
          f"Status: {info['status']} | Payload: {info['payload_kg']}kg")
