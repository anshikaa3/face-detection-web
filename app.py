import streamlit as st
import cv2
import numpy as np
import os

st.title("Face Detection + Recognition Web App")
st.write("Upload an image and recognize trained faces.")

DATASET_PATH = "dataset"

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# -------------------------------
# TRAINING SECTION
# -------------------------------

faces = []
labels = []
label_map = {}
current_label = 0

if os.path.exists(DATASET_PATH):
    for person_name in os.listdir(DATASET_PATH):
        person_path = os.path.join(DATASET_PATH, person_name)

        if os.path.isdir(person_path):
            label_map[current_label] = person_name

            for image_name in os.listdir(person_path):
                img_path = os.path.join(person_path, image_name)
                img = cv2.imread(img_path)

                if img is None:
                    continue

                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                detected = face_cascade.detectMultiScale(
                    gray_img,
                    scaleFactor=1.2,
                    minNeighbors=6,
                    minSize=(80, 80)
                )

                # Take only first detected face per image
                if len(detected) > 0:
                    (x, y, w, h) = detected[0]
                    face = gray_img[y:y+h, x:x+w]
                    face = cv2.resize(face, (200, 200))
                    faces.append(face)
                    labels.append(current_label)

            current_label += 1

st.write("Total trained faces:", len(faces))

# Train recognizer
if len(faces) > 0:
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(labels))
else:
    recognizer = None

# -------------------------------
# IMAGE UPLOAD SECTION
# -------------------------------

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    detected_faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=8,
        minSize=(100, 100)
    )

    # Keep only largest face (avoid duplicate small boxes)
    if len(detected_faces) > 1:
        detected_faces = sorted(
            detected_faces,
            key=lambda x: x[2] * x[3],
            reverse=True
        )
        detected_faces = detected_faces[:1]

    for (x, y, w, h) in detected_faces:

        face_roi = gray[y:y+h, x:x+w]
        face_roi = cv2.resize(face_roi, (200, 200))

        if recognizer is not None:
            label, confidence = recognizer.predict(face_roi)

            # Lower confidence = better match
            if confidence < 80:
                name = label_map.get(label, "Unknown")
            else:
                name = "Unknown"

            text = f"{name} | Confidence: {round(confidence,2)}"
        else:
            text = "No trained data"

        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(
            image,
            text,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    st.image(image, channels="BGR")
    st.success(f"Detected {len(detected_faces)} face(s)")
