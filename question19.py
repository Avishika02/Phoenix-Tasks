# Q19) Simulate an aerial drone view: draw an 8x8 grid over an image,
# and let the user click a cell to highlight it and print its coordinates.
#
# NOTE: cv2.imshow() requires a GUI window, so this works directly in VS Code
# or a local Python install. Google Colab does NOT support cv2.imshow() or
# clickable OpenCV windows at all (it has no display) -- so for Colab, this
# exact script will NOT work as-is. Run this one on VS Code or a local
# Python/compiler with a display instead.

import cv2

# Load any image (acts as the simulated aerial view from the drone)
img = cv2.imread("sample.jpg")
clone = img.copy()  # keep an untouched copy so we can redraw fresh each click

height, width = img.shape[:2]

GRID_SIZE = 8                       # 8x8 grid
cell_w = width // GRID_SIZE         # width of each grid cell in pixels
cell_h = height // GRID_SIZE        # height of each grid cell in pixels


def draw_grid(image):
    """Draws an 8x8 white grid of lines over the given image."""
    # Draw vertical lines
    for i in range(1, GRID_SIZE):
        x = i * cell_w
        cv2.line(image, (x, 0), (x, height), (255, 255, 255), 1)
    # Draw horizontal lines
    for i in range(1, GRID_SIZE):
        y = i * cell_h
        cv2.line(image, (0, y), (width, y), (255, 255, 255), 1)


def mouse_callback(event, x, y, flags, param):
    """Handles mouse click events on the image window."""
    if event == cv2.EVENT_LBUTTONDOWN:  # respond only to left mouse button click
        # Figure out which grid cell (row, col) was clicked based on pixel position
        col = x // cell_w
        row = y // cell_h

        print(f"Clicked at: x={x}, y={y} -> Grid Cell: (row={row}, col={col})")

        # Start fresh from the clean grid image so old highlights don't stack up
        display_img = clone.copy()
        draw_grid(display_img)

        # Highlight the selected cell with a filled blue rectangle (semi-opaque look)
        cell_x1, cell_y1 = col * cell_w, row * cell_h
        cell_x2, cell_y2 = cell_x1 + cell_w, cell_y1 + cell_h
        overlay = display_img.copy()
        cv2.rectangle(overlay, (cell_x1, cell_y1), (cell_x2, cell_y2), (255, 0, 0), -1)
        # Blend the overlay with the original for a semi-transparent highlight effect
        cv2.addWeighted(overlay, 0.4, display_img, 0.6, 0, display_img)

        # Display the cell coordinates as text near the click point
        cv2.putText(display_img, f"({row},{col})", (cell_x1 + 5, cell_y1 + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        cv2.imshow("Aerial View", display_img)
        # Also save the latest highlighted result to disk so it can be checked headlessly
        cv2.imwrite("aerial_view_clicked.jpg", display_img)


# --- Set up initial display ---
draw_grid(img)
cv2.imshow("Aerial View", img)
cv2.setMouseCallback("Aerial View", mouse_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()
