from PIL import Image, ImageDraw, ImageFont
import requests

def fetch_detections(api_url, image_path):
    # Open image from local file path
    with open(image_path, 'rb') as img_file:
        files = {'image': img_file}
        response = requests.post(api_url, files=files)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching detections: {response.status_code}")
            return None

def draw_boxes_on_image(image_path, detections):
    # Open image from local file path
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()

    # Draw bounding boxes and labels
    for obj in detections['objects']:
        x1 = obj['x1']
        y1 = obj['y1']
        x2 = obj['x2']
        y2 = obj['y2']
        class_name = obj['class']
        confidence = obj['confidence']

        # Draw the bounding box
        draw.rectangle([x1, y1, x2, y2], outline='red', width=2)

        # Draw the label
        label = f"{class_name} ({confidence:.2f})"
        draw.text((x1, y1), label, fill='red', font=font)

    # Save or show the image
    img.show()  # To display the image
    # img.save('output_image.jpg')  # To save the image

if __name__ == "__main__":
    # Example local image path and API URL
    image_path = "./images/cycles.jpg"
    api_url = "http://127.0.0.1:10000/detect"

    detections = fetch_detections(api_url, image_path)
    if detections:
        draw_boxes_on_image(image_path, detections)
