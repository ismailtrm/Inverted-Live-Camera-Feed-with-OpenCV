import cv2
import numpy as np
import collections

# Start the camera
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Cannot open camera!")
    exit()

# Get the camera FPS (frames per second)
fps = cap.get(cv2.CAP_PROP_FPS)
delay_time = 3  # 3-second delay
buffer_size = int(fps * delay_time)

# Create a frame buffer with a max size corresponding to the delay
frame_buffer = collections.deque(maxlen=buffer_size)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # If the frame is not read correctly, exit the loop
    if not ret:
        print("Error: Cannot retrieve frame!")
        break

    # Invert the colors of the frame
    inverted = 255 - frame

    # Add the inverted frame to the buffer
    frame_buffer.append(inverted)

    # If the buffer is full, blend the oldest frame with the current one
    if len(frame_buffer) == buffer_size:
        image_new = cv2.addWeighted(frame, 0.5, frame_buffer[0], 0.5, 0)
        cv2.imshow('Inverted & Time-Shifted Camera', image_new)
    else:
        # If the buffer is not full yet, show the current frame
        cv2.imshow('Inverted & Time-Shifted Camera', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
