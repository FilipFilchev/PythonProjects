
### BASIC CV2 


import cv2

# Open the default camera (camera number 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # If the frame was not read correctly, break the loop
    if not ret:
        break

    # Display the frame in a window called 'Camera Feed'
    cv2.imshow('Camera Feed', frame)

    # If 'q' is pressed on the keyboard, break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
