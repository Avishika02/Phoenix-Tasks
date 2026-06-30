# Q8) Restricted Airspace Conflict Checker
# Sets are ideal here because zone membership/overlap checks are needed, order doesn't matter,
# and duplicates are not meaningful for zone names.

planned_zones = {"Z1", "Z2", "Z3", "Z5", "Z7"}
restricted_zones = {"Z3", "Z5", "Z6", "Z8"}
cleared_zones = {"Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8"}

# 1. Find which planned zones are restricted (intersection)
conflict_zones = planned_zones & restricted_zones   # '&' operator = set intersection
print("Planned zones that are restricted (conflicts):", conflict_zones)

# 2. Find zones that are planned but NOT restricted (safe zones)
safe_zones = planned_zones - restricted_zones        # '-' operator = set difference
print("Safe planned zones (not restricted):", safe_zones)

# 3. Zones in either planned or restricted, but NOT both (symmetric difference)
sym_diff_zones = planned_zones ^ restricted_zones     # '^' operator = symmetric difference
print("Zones in exactly one of planned/restricted:", sym_diff_zones)

# 4. Check if planned_zones is a subset of cleared_zones
is_subset = planned_zones.issubset(cleared_zones)     # .issubset() checks containment
if is_subset:
    print("All planned zones are cleared for flight.")
else:
    print("WARNING: Some planned zones are NOT cleared!")

# 5. Add "Z9" to planned_zones and remove "Z7" (added by mistake)
planned_zones.add("Z9")     # .add() inserts a single element into a set
planned_zones.discard("Z7") # .discard() removes an element safely (no error if missing)
print("\nUpdated planned_zones:", planned_zones)

# 6. Print the count of unique zones across all three sets combined
all_zones = planned_zones | restricted_zones | cleared_zones  # '|' operator = union
print("Total unique zones across all sets:", len(all_zones))
