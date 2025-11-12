# 🧠 YOLOv8 Virtual Storage - Waste Classification Project

This project implements **YOLOv8 (You Only Look Once)** for **waste material classification** using a custom dataset.  
It helps in identifying and sorting waste into categories like **Plastic, Metal, Glass, Paper, Cardboard, and Biodegradable**, supporting smart waste management systems.

---

## 📁 Project Structure
waste-classification-yolov8/
├── data/
│ ├── train/
│ ├── valid/
│ ├── test/
│ └── data.yaml
├── runs/
├── models/
└── train.py


---

## 🚀 Features
- Trains YOLOv8 model on custom waste dataset  
- Supports real-time image and video detection  
- Dataset prepared from **Kaggle & Roboflow**  
- Detects 6 waste types:  
  - BIODEGRADABLE  
  - CARDBOARD  
  - GLASS  
  - METAL  
  - PAPER  
  - PLASTIC  

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Ajit-programmer/YOLOv8-Virtual-Storage.git
cd YOLOv8-Virtual-Storage

2. Create a virtual environment
python -m venv venv
venv\Scripts\activate      # For Windows
3. Install dependencies
pip install -r requirements.txt
4. Train the model
yolo task=detect mode=train model=yolov8n.pt data=data/data.yaml epochs=50 imgsz=640
5. Run detection
yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=your_image.jpg
.
.
.

🧩 Dataset Info

Dataset used: Garbage Classification - Roboflow Dataset

Format: YOLOv8 with data.yaml configuration.



🧠 Model Info

Model: YOLOv8n

Framework: Ultralytics YOLO

Losses tracked: Box, Class, DFL

Training Epochs: 50


📊 Future Improvements

Add web interface for live detection

Integrate cloud storage for model outputs

Deploy model as an API using Flask/FastAPI

🏆 License

This project is licensed under CC BY 4.0 (Open Source).
Feel free to use, modify, and contribute!


👨‍💻 Author

Ajit G.
“Turning waste into data-driven insights.”
GitHub: Ajit-programmer

---

Would you like me to make it a bit **shorter and more aesthetic** with emojis and markdown highlights for GitHub display?
