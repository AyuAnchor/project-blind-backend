from flask import Flask, request, jsonify
import cv2
import numpy as np
from flask_cors import CORS
from ultralytics import YOLO

app = Flask(__name__)
CORS(app)  # To allow cross-origin requests

# Load YOLOv8 model
model = YOLO('weights/yolov8n.pt')  # Use a YOLOv8 model (e.g., 'yolov8n.pt' for YOLOv8 nano)

@app.route('/detect', methods=['POST'])
def detect_objects():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    # Read the image from the request
    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Perform object detection
    results = model(img)
    
    # Extract results
    detections = results[0].boxes.xyxy.cpu().numpy()  # x1, y1, x2, y2, confidence, class
    classes = results[0].boxes.cls.cpu().numpy()
    confidences = results[0].boxes.conf.cpu().numpy()
    
    objects = []
    for i in range(len(detections)):
        x1, y1, x2, y2 = detections[i]
        objects.append({
            'x1': int(x1),
            'y1': int(y1),
            'x2': int(x2),
            'y2': int(y2),
            'confidence': float(confidences[i]),
            'class': model.names[int(classes[i])]
        })
    
    return jsonify({'objects': objects})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
