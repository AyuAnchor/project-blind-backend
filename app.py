from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from helpers import draw_boxes_on_image
from yolo_utils import get_detections
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # To allow cross-origin requests

@app.route('/detect', methods=['POST'])
def detect_objects():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    # Read the image from the request
    file = request.files['image']
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    # Load the image as a PIL Image
    try:
        img = Image.open(file)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    # Get detections
    detections = get_detections(img)

    # Get 'download' query parameter
    download = request.args.get('download', 'false').lower() in ['true', '1']

    if download:
        image = draw_boxes_on_image(img, detections)
        # Save the image to a BytesIO object
        img_io = io.BytesIO()
        image.save(img_io, 'JPEG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='detected_image.jpg')

    else:
        # Return JSON with detection results
        return jsonify(detections)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
