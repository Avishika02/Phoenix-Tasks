# Q11) Recursive Waypoint Distance Calculator
# Pure recursion only -- no loops used anywhere

waypoints = [(0, 0), (3, 4), (6, 8), (10, 8), (10, 0)]


def total_distance(waypoints, index=0):
    """
    Recursively computes total path distance across all waypoints.
    Base case: if we're at (or past) the second-to-last waypoint, there's only
    one segment left or none left, so we stop recursing.
    """
    # Base case: if there's only one waypoint left (or none), no distance to add
    if index >= len(waypoints) - 1:
        return 0

    # Get current point and the next point
    x1, y1 = waypoints[index]
    x2, y2 = waypoints[index + 1]

    # Euclidean distance formula between the two points
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Recursive case: this segment's distance + distance of the rest of the path
    return distance + total_distance(waypoints, index + 1)


def find_longest_leg(waypoints, index=0, max_dist=0):
    """
    Recursively finds the longest single leg (segment) in the journey.
    Carries the current maximum found so far as an accumulator argument.
    """
    # Base case: if there's only one waypoint left (or none), return the max found so far
    if index >= len(waypoints) - 1:
        return max_dist

    # Calculate distance of the current leg
    x1, y1 = waypoints[index]
    x2, y2 = waypoints[index + 1]
    current_leg = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Update max_dist if this leg is longer than what we've seen so far
    new_max = max(max_dist, current_leg)

    # Recurse into the next leg, carrying forward the updated max
    return find_longest_leg(waypoints, index + 1, new_max)


# --- Run and display results ---
print("Total path distance:", round(total_distance(waypoints), 2))
print("Longest single leg:", round(find_longest_leg(waypoints), 2))
