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

                detected = face_cascade.detectMultiScale(gray_img, 1.3, 5)

                for (x, y, w, h) in detected:
                    face = gray_img[y:y+h, x:x+w]
                    face = cv2.resize(face, (200, 200))
                    faces.append(face)
                    labels.append(current_label)

            current_label += 1
