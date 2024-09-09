from PIL import ImageDraw, ImageFont

def draw_boxes_on_image(image, detections):
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()

    for obj in detections['objects']:
        x1 = obj['x1']
        y1 = obj['y1']
        x2 = obj['x2']
        y2 = obj['y2']
        class_name = obj['class']
        confidence = obj['confidence']

        draw.rectangle([x1, y1, x2, y2], outline='red', width=2)
        label = f"{class_name} ({confidence:.2f})"
        draw.text((x1, y1), label, fill='red', font=font)

    return image
