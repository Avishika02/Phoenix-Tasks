# Q3) Drone specs program: max payload, type() of each var,
# payload sufficiency check, and weight conversion to grams (int)

# Given drone specifications
max_takeoff_weight = 4.5      # kg, float -> heaviest the drone can legally take off at
frame_weight = 1.2            # kg, float -> weight of the drone's body/frame
battery_weight = 0.8          # kg, float -> weight of the battery pack
num_propellers = 4            # int -> number of propellers (not directly used in weight calc)
motor_weight = 0.075          # kg per motor, float -> weight of a SINGLE motor
is_gps_enabled = True         # bool -> whether GPS module is fitted
gps_module_weight = 0.05      # kg, float -> weight of GPS module (only counts if enabled)

# 1. Calculate the maximum payload the drone can carry
# Total fixed weight = frame + battery + (motor_weight * number of motors, assume 1 motor per propeller)
total_motor_weight = motor_weight * num_propellers          # 4 motors total weight
gps_weight = gps_module_weight if is_gps_enabled else 0      # only add GPS weight if it's actually fitted

fixed_weight = frame_weight + battery_weight + total_motor_weight + gps_weight
max_payload = max_takeoff_weight - fixed_weight              # whatever weight budget remains is payload capacity

print(f"Maximum payload the drone can carry: {max_payload:.3f} kg")

# 2. Print the type() of each variable
print("\nVariable Types")
print("max_takeoff_weight:", type(max_takeoff_weight))
print("frame_weight:", type(frame_weight))
print("battery_weight:", type(battery_weight))
print("num_propellers:", type(num_propellers))
print("motor_weight:", type(motor_weight))
print("is_gps_enabled:", type(is_gps_enabled))
print("gps_module_weight:", type(gps_module_weight))

# 3. Check whether payload is enough to carry a 1.8 kg camera (print bool)
camera_weight = 1.8
can_carry_camera = max_payload >= camera_weight  # boolean result: True/False
print(f"\nCan the drone carry a 1.8 kg camera? {can_carry_camera}")

# 4. Convert max_takeoff_weight to grams and store as an int
max_takeoff_weight_grams = int(max_takeoff_weight * 1000)  # kg -> g, then truncate to int
print(f"\nMax takeoff weight in grams (int): {max_takeoff_weight_grams}")
print("Type of converted value:", type(max_takeoff_weight_grams))