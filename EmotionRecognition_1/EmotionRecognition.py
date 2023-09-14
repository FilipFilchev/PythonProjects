"""
FIX THE SPEED and UPLOAD better MODEL.h5

the II code which is the first test is actually better now...
"""


# Step 2: Import required libraries
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array


# Step 3: Load a pre-trained emotion recognition model
# You can use a model that you have trained, or you can download a pre-trained model.
# Here, let's assume that you have a model named 'emotion_model.h5'.

model = load_model('emotion_model.h5')

# Step 4: Define the list of emotion labels
emotion_labels = ['Angry', 'Disgust', 'Scared', 'Happy', 'Sad', 'Surprised', 'Neutral']

# Step 5: Open the webcam and start emotion recognition
#use OpenCV to capture the webcam feed.

camera = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = camera.read()

    # If the frame was not read correctly, break the loop
    if not ret:
        break
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Use OpenCV's cascade classifier to detect faces in the image
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    # For each face detected, predict the emotion
    for (x, y, w, h) in faces:
        # Extract the region of interest (ROI) of the face
        roi = frame[y:y + h, x:x + w]  # This now has shape (h, w, 3)

       # Resize and preprocess the ROI
        roi = cv2.resize(roi, (224, 224))  # Resizing to match model's expected input shape
        roi = roi.astype("float") / 255.0  # Normalizing pixel values
        roi = np.expand_dims(roi, axis=0)  # Expanding dimensions for model input

        # Make the emotion prediction
        preds = model.predict(roi)[0]
        emotion = emotion_labels[preds.argmax()]

        # Draw a rectangle around the face and emotion label
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Human is ...", frame)

    # If 'q' key is pressed, break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
camera.release()
cv2.destroyAllWindows()










#  TRYOUT step by step test driven run:


# Step 1: Import required libraries
# import cv2
# from mtcnn import MTCNN
# from deepface import DeepFace

# # Step 2: Instantiate the face detector
# detector = MTCNN()

# # Step 3: Open the webcam
# camera = cv2.VideoCapture(0)

# while True:
#     # Step 4: Read a frame from the webcam
#     ret, frame = camera.read()

#     # If the frame was not read correctly, break the loop
#     if not ret:
#         break

#     # Step 5: Detect faces using MTCNN
#     faces = detector.detect_faces(frame)

#     # Step 6: For each face detected, predict the emotion using DeepFace
#     for face in faces:
#         x, y, w, h = face['box']
#         roi = frame[y:y+h, x:x+w]

#         # Step 7: Use DeepFace to predict the emotion of the face
#         result = DeepFace.analyze(roi, actions = ['emotion'], enforce_detection = False)

#         #RESULT
#         print(result)
#         print(f"Dominant Emotion is: {result[0]['dominant_emotion']}")
#         print(dict(result[0]['emotion']))
#         """
#        # TRY TO  Extract the predicted emotion
       
#         try:
#             # assert isinstance(result[0], dict), f"Expected dict, got {type(result['emotion'])}"
#             print(f"Expected dict, got {type(result[0]['emotion'])}")
#             #TRYOUT
#             #Action: emotion: 100%|███████████████████████████████████████████████| 1/1 [00:00<00:00,  9.24it/s]
#             [
#                 {'emotion': {'angry': 12.641555070877075, 'disgust': 0.01593762426637113, 'fear': 3.229586035013199, 'happy': 0.18768556183204055, 'sad': 28.306886553764343, 'surprise': 0.12708732392638922, 'neutral': 55.491262674331665},
#                  'dominant_emotion': 'neutral', 
#                  'region': {'x': 0, 'y': 0, 'w': 302, 'h': 402}
#                  }
#             ]
        
#             emotion = result[0]["dominant_emotion"]
#             ###

#             #emotion = max(result['emotion'], key=result['emotion'].get)

#         except AssertionError as error:
#             print(error)
#             print(f"Unexpected result: {result[0]}")
#             raise
#         except Exception as error:
#             print(f"An error occurred: {error}")
#             raise
#         """
#         print(f"Angry : {result[0]['emotion']['angry']}")
        
#         # Memory allocation : 
#         angry = int(result[0]['emotion']['angry'])
#         print(max(result[0]['emotion']['sad'], angry))

#         emotion = result[0]["dominant_emotion"]
#         # Draw a rectangle around the face and the emotion label
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#     # Step 8: Display the frame
#     cv2.imshow('Emotion Recognition', frame)

#     # If 'q' key is pressed, break the loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Clean up
# camera.release()
# cv2.destroyAllWindows()


