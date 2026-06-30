# Q17) Detect a rectangular landing pad (white rectangle on dark background)
# from a drone camera feed image, and "land" there.

import cv2

# Load the camera feed image (replace with actual drone camera frame/path)
img = cv2.imread("landing_pad_sample.jpg")

# Convert the image to grayscale -- simplifies thresholding since we just
# need brightness info, not colour, to separate white pad from dark ground
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding: any pixel brighter than 200 becomes white (255),
# everything else becomes black (0). This isolates the white landing pad.
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Find contours (outlines of connected white regions) in the thresholded image
# RETR_EXTERNAL = only outer contours, CHAIN_APPROX_SIMPLE = compress contour points
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

landing_pad_found = False  # flag to track if we successfully found a pad

# Loop through every detected contour shape
for cnt in contours:
    # Approximate the contour shape to a polygon with fewer vertices
    # epsilon controls how "loose" the approximation is (2% of perimeter here)
    epsilon = 0.02 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    # A rectangle should approximate to exactly 4 vertices/corners
    if len(approx) == 4:
        area = cv2.contourArea(cnt)
        # Ignore tiny noise contours -- require a reasonably large area
        if area > 500:
            # Get bounding box coordinates of this rectangle
            x, y, w, h = cv2.boundingRect(approx)

            # Draw a green rectangle around the detected landing pad for visualization
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(img, "Landing Pad", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            landing_pad_found = True
            break  # stop after finding the first valid rectangular pad

# Print landing status based on whether a pad was found
if landing_pad_found:
    print("Landing pad detected. Landing...")
else:
    print("No landing pad detected. Aborting landing.")

# Save the annotated result image as required
cv2.imwrite("sahi.jpg", img)
print("Result saved as sahi.jpg")
