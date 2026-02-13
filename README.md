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
2. Image is converted to a NumPy array  
3. Converted to grayscale for better detection  
4. Haar Cascade classifier scans the image  
5. Faces are detected using feature-based detection  
6. Bounding boxes are drawn around detected faces  
7. Final processed image is displayed  

---

## 🛠️ Tech Stack

- Python 3.13
- Streamlit (Web UI + Deployment)
- OpenCV (Computer Vision)
- NumPy (Image Processing)
- Haar Cascade Classifier (Face Detection)
- Git & GitHub
- Streamlit Cloud (Hosting)

---

## 🔍 Face Detection Method Used

This project uses the **Haar Cascade Classifier**, which:

- Is a pre-trained XML model from OpenCV
- Uses feature-based detection (edges & line detection)
- Applies a sliding window approach
- Efficient for static image detection
- Lightweight and fast compared to deep learning models

---

## 📦 Installation (Run Locally)

```bash
git clone https://github.com/anshikaa3/face-detection-web.git
cd face-detection-web

python -m venv venv
venv\Scripts\activate  # On Windows

pip install -r requirements.txt
streamlit run app.py
