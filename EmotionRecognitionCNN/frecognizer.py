import cv2
from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
import numpy as np

# Load model
xml = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
model = load_model('./model.h5')
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprised']  # Rename this variable

# Open cam
cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    
    # Grayscale 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = xml.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)  # Resized to 48x48, the expected input

        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype("float") / 255.0  # Normalizing
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)  # Expanding dimensions for model input

            prediction = model.predict(roi)[0]
            emotion = emotion_labels[prediction.argmax()]  
            label_position = (x, y)
            cv2.putText(frame, emotion, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print(f"Human is {emotion}")
        else:
            cv2.putText(frame, '0 Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Human is ...", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop cam
cam.release()
# Close window
cv2.destroyAllWindows()


"""Result:
1/1 [==============================] - 2s 2s/step
Human is Neutral
1/1 [==============================] - 0s 365ms/step
Human is Neutral
1/1 [==============================] - 0s 120ms/step
Human is Neutral
1/1 [==============================] - 0s 135ms/step
Human is Happy
1/1 [==============================] - 0s 110ms/step
Human is Happy
1/1 [==============================] - 0s 99ms/step
Human is Happy
1/1 [==============================] - 0s 109ms/step
Human is Sad
1/1 [==============================] - 0s 107ms/step
Human is Neutral
1/1 [==============================] - 0s 124ms/step
Human is Sad
1/1 [==============================] - 0s 100ms/step
Human is Sad
1/1 [==============================] - 0s 118ms/step
Human is Sad
1/1 [==============================] - 0s 130ms/step
Human is Sad
1/1 [==============================] - 0s 198ms/step
Human is Happy
1/1 [==============================] - 0s 159ms/step
Human is Happy
1/1 [==============================] - 0s 208ms/step
Human is Surprised
1/1 [==============================] - 0s 225ms/step
Human is Happy
1/1 [==============================] - 0s 140ms/step
Human is Neutral
1/1 [==============================] - 0s 112ms/step
Human is Surprised
1/1 [==============================] - 0s 211ms/step
Human is Sad

"""

#test it yourself