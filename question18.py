# Q18) Simulate a drone camera tracking a red object using HSV colour filtering.
# Since we don't have a live camera feed here, this reads a static test image,
# but the same logic applies frame-by-frame to a video capture loop (commented below).

import cv2
import numpy as np

# --- Load a single frame (replace with cv2.VideoCapture(0) for a live webcam feed) ---
frame = cv2.imread("red_object_sample.jpg")

# Convert frame from BGR colour space to HSV
# HSV (Hue, Saturation, Value) makes colour-based filtering much easier than
# RGB/BGR because Hue alone represents the "pure colour", unaffected by lighting
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Define HSV ranges for the colour red
# Red wraps around the Hue circle (0 and 180 in OpenCV's 0-180 scale), so we
# need TWO ranges to fully capture all shades of red
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# Create masks for both red ranges and combine them with bitwise OR
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)

# Find contours of the red regions in the mask
contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

object_detected = False  # flag for whether we found a valid red object this frame

if contours:
    # Pick the largest contour, assuming it's the main object (ignores small red noise)
    largest_contour = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(largest_contour)

    if area > 300:  # ignore tiny specks of red below this area threshold
        # Get the minimum enclosing circle around the detected red blob
        (cx, cy), radius = cv2.minEnclosingCircle(largest_contour)
        center = (int(cx), int(cy))
        radius = int(radius)

        # Draw a circle around the detected red object
        cv2.circle(frame, center, radius, (0, 255, 0), 2)
        cv2.circle(frame, center, 3, (0, 0, 255), -1)  # small dot at the exact center

        object_detected = True

# Overlay status text on the frame based on detection result
if object_detected:
    cv2.putText(frame, "Object Detected", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    print("Object Detected")
else:
    cv2.putText(frame, "Object Lost", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    print("Object Lost")

cv2.imwrite("red_object_tracking_result.jpg", frame)
print("Result saved as red_object_tracking_result.jpg")

# --- For a LIVE webcam version, wrap the above logic in a loop like this: ---
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     # ... (same HSV masking + contour + circle-drawing logic here) ...
#     cv2.imshow("Red Object Tracking", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):   # press 'q' to quit
#         break
# cap.release()
# cv2.destroyAllWindows()
