# Q2) Take the drone's body weight (in kg) and payload weight (in kg) as input,
# output the total weight and print whether it's greater than 2kg or not.
# (Creativity: taking input in grams and converting to kg)

# Take body weight in grams from the user, convert string -> float
body_weight_g = float(input("Enter body weight (in grams): "))

# Take payload weight in grams from the user
payload_weight_g = float(input("Enter payload weight (in grams): "))

# Convert both values from grams to kilograms (1 kg = 1000 g)
body_weight_kg = body_weight_g / 1000
payload_weight_kg = payload_weight_g / 1000

# Calculate the total weight by adding both kg values
total_weight = body_weight_kg + payload_weight_kg

# Print total weight, rounded to 2 decimal places for clean output
print(f"Total weight: {total_weight:.2f} kg")

# Check condition and print appropriate message
if total_weight > 2:
    print("Total weight is greater than 2 kg")
elif total_weight == 2:
    print("Total weight is exactly 2 kg")
else:
    print("Total weight is less than 2 kg")
