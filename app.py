from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

model = YOLO("best.pt")   # your trained YOLO model

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return "No file uploaded"

    file = request.files["image"]
    if file.filename == "":
        return "No selected file"

    # Save file
    unique_name = str(uuid.uuid4()) + ".jpg"
    image_path = os.path.join(UPLOAD_FOLDER, unique_name)
    file.save(image_path)

    # Predict
    results = model.predict(source=image_path, conf=0.25)

    detected_label = "Unknown"
    confidence = 0

    for r in results:
        if r.boxes:
            box = r.boxes[0]
            cls = int(box.cls[0])
            confidence = float(box.conf[0])
            detected_label = model.names[cls]

    return render_template(
        "result.html",
        uploaded_image=image_path,
        label=detected_label,
        conf=round(confidence, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)
