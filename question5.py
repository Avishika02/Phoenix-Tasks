# Q5) Flight Path Analyser

altitudes = [0, 15, 42, 78, 120, 118, 115, 50, 20, 0]

# 1. Find the maximum altitude and the index (the "second") it occurred at
max_altitude = max(altitudes)             # built-in max() gives the highest value
max_index = altitudes.index(max_altitude) # .index() gives position of first occurrence
print(f"Maximum altitude: {max_altitude}m occurred at index (second): {max_index}")

# 2. Calculate the average altitude, rounded to 2 decimal places
average_altitude = round(sum(altitudes) / len(altitudes), 2)
print(f"Average altitude: {average_altitude}m")

# 3. Create climb_rates list where each element = altitudes[i+1] - altitudes[i]
climb_rates = []
for i in range(len(altitudes) - 1):          # stop one before the end to avoid index error
    rate = altitudes[i + 1] - altitudes[i]   # difference between consecutive readings
    climb_rates.append(rate)
print("Climb rates between consecutive seconds:", climb_rates)

# 4. Find the steepest climb (max positive rate) and steepest descent (min/most negative rate)
steepest_climb = max(climb_rates)
steepest_descent = min(climb_rates)
print(f"Steepest climb: {steepest_climb}m/s")
print(f"Steepest descent: {steepest_descent}m/s")

# 5. Remove all zero-altitude entries and print the trimmed path
# List comprehension: keep only values that are not equal to 0
trimmed_path = [alt for alt in altitudes if alt != 0]
print("Trimmed flight path (zero-altitude entries removed):", trimmed_path)
