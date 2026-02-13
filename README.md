# 👁️ Face Detection Web App

A cloud-deployed Face Detection Web Application built using **Streamlit and OpenCV**.  
This application allows users to upload an image and automatically detects human faces using a pre-trained Haar Cascade classifier.

---

## 🚀 Live Demo

👉 https://face-detection-web-nh7azu28f5g8qgzfgbmlep.streamlit.app/

---

## 🧠 Project Overview

This project demonstrates how classical computer vision techniques can be integrated into a web application and deployed to the cloud.

The application:

- Accepts image uploads from users
- Converts images to grayscale
- Detects faces using Haar Cascade Classifier
- Draws bounding boxes around detected faces
- Displays processed output image in the browser

This project showcases:

- Computer Vision fundamentals
- OpenCV integration in Python
- Cloud deployment using Streamlit
- Real-time image processing workflow
- Production-ready dependency handling

---

## 🏗️ System Architecture

1. User uploads an image via Streamlit UI  
2. Image is converted into a NumPy array  
3. Converted to grayscale for improved detection accuracy  
4. Haar Cascade classifier scans the image  
5. Faces are detected using feature-based detection  
6. Bounding boxes are drawn around detected faces  
7. Final processed image is displayed  

---

## 🛠️ Tech Stack

- Python 3
- Streamlit (Web UI + Deployment)
- OpenCV (Computer Vision)
- NumPy (Image Processing)
- Haar Cascade Classifier (Face Detection)
- Git & GitHub
- Streamlit Cloud (Hosting)

---

## 🔍 Face Detection Method Used

This project uses the **Haar Cascade Classifier**, a classical machine learning-based object detection algorithm.

### How it works:

- Uses a pre-trained XML model from OpenCV
- Detects facial features like edges and line patterns
- Applies sliding window detection across the image
- Uses cascade stages to quickly eliminate non-face regions
- Returns bounding box coordinates of detected faces

Haar Cascade is lightweight and fast for static image detection.  
While deep learning models provide higher accuracy, Haar Cascade is efficient for quick and simple deployments.

---

## 📦 Installation (Run Locally)

```bash
git clone https://github.com/anshikaa3/face-detection-web.git
cd face-detection-web

python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
streamlit run app.py
```

The app will run at:

```
http://localhost:8501
```

---

## 🌍 Deployment Details

- Deployed using Streamlit Cloud
- Uses `opencv-python-headless` for cloud compatibility
- Dependencies managed via `requirements.txt`
- Automatically rebuilds on every GitHub push
- Runs without GUI support in server environment

Live App:
👉 https://face-detection-web-nh7azu28f5g8qgzfgbmlep.streamlit.app/

---

## 📊 Features

- Upload image from local system
- Detect multiple faces in a single image
- Draw bounding boxes around detected faces
- Display total number of faces detected
- Cloud-hosted and publicly accessible

---

## ⚠️ Why opencv-python-headless?

Cloud servers do not support GUI rendering.  
The standard `opencv-python` package depends on GUI libraries which cause errors in cloud environments.

To resolve this, the project uses:

```
opencv-python-headless
```

This version removes GUI dependencies and works perfectly in headless (server) environments like Streamlit Cloud.

---

## 📈 Future Enhancements

- Add real-time webcam detection
- Integrate Face Recognition (LBPH / Deep Learning)
- Add confidence score display
- Allow downloading processed image
- Improve UI/UX design
- Containerize using Docker

---

## 🎯 Key Learnings

Through this project, I learned:

- Image preprocessing using OpenCV
- Classical face detection techniques
- Handling Python virtual environments
- Cloud deployment challenges
- Using headless OpenCV for server environments
- Debugging dependency issues in production
- Structuring production-ready repositories

---

## 👩‍💻 Author

**Anshika Srivastava**  
GitHub: https://github.com/anshikaa3  

---

