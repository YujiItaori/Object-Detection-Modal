# 🎥 Real-Time Object Detection with Flask & YOLOv5

This is a Python web application that performs real-time object detection through your webcam using YOLOv5 and displays the output via a Flask frontend.

## 🚀 Features

- 🔍 Detects objects using YOLOv5 (`yolov5s.pt`)
- 🎥 Captures live webcam video feed
- 🧠 Performs real-time inference
- 🌐 Web interface built with Flask

## 🛠️ Tech Stack

- Python
- OpenCV
- YOLOv5 (PyTorch)
- Flask

## 📦 Installation

Clone the repo:
```bash
git clone https://github.com/yourusername/cam-detect-app.git
cd cam-detect-app

## Set up virtual environment:

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

## Clone YOLOv5 inside the folder:

git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
cd ..

## Run the app:
python app.py or flask run

## 📸 Result
Open in browser: http://127.0.0.1:5000

## 📂 Folder Structure
cam-detect-app/
├── app.py
├── camera.py
├── detector.py
├── yolov5/
├── templates/
│   └── index.html

## 📃 License
MIT — free to use for personal or commercial purposes.