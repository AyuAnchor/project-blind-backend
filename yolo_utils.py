from ultralytics import YOLO

# Load YOLO11 model
model = YOLO('weights/yolo11l.pt')  # Use a YOLO11 model (e.g., 'yolo11n.pt' for YOLO11 nano)

def get_detections(img):
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
    
    return {'objects': objects}
