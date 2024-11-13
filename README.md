# Flask YOLO11 Object Detection API

This project provides a Flask-based API for object detection using the YOLO11 model. The API allows users to upload images and receive either JSON data with detection results or a downloadable image with bounding boxes drawn around detected objects.

## Features

- **Upload Image**: Accepts image files for object detection.
- **Detection Results**: Provides object detection results in JSON format.
- **Image with Detections**: Optionally returns an image with bounding boxes and labels drawn on detected objects.
- **Cross-Origin Requests**: Supports CORS to allow access from different origins.

## Prerequisites

- Python 3.7+
- Flask
- Flask-CORS
- Ultralytics YOLO11
- Pillow

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/AyuAnchor/project-blind-backend.git
   cd project-blind-backend
   ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask Application:**

    ```bash
    python app.py
    ```
    The server will start and listen on http://localhost:10000.


2. **Make a POST Request to /detect:**

    - To receive JSON data:

        ```bash
        curl -X POST http://localhost:10000/detect -F "image=@path/to/your/image.jpg"
        ```

    - To download the image with detections:
        ```bash
        curl -X POST "http://localhost:10000/detect?download=true" -F "image=@path/to/your/image.jpg" --output detected_image.jpg
        ```


## API Endpoints

### 1. Detect Objects - JSON Response
- **Endpoint:** `/detect`
- **Method:** `POST`
- **Description:** Upload an image, and the API returns a JSON response containing the detected objects with their bounding box coordinates, class names, and confidence scores.
- **Request Parameters:**
  - **image**: (file) The image file to be processed.
- **Query Parameters:**
  - **download**: (optional, boolean) If set to `true`, the API will return the image with detected objects marked and allow you to download it. Default is `false`.
- **Response:**
  - **Content-Type:** `application/json`
  - **Sample Response:**
    ```json
    {
      "objects": [
        {
          "x1": 34,
          "y1": 50,
          "x2": 200,
          "y2": 300,
          "confidence": 0.85,
          "class": "person"
        },
        ...
      ]
    }
    ```

### 2. Detect Objects - Image Response
- **Endpoint:** `/detect`
- **Method:** `POST`
- **Description:** Upload an image, and the API returns the image with detected objects marked. This is intended for cases where the user wants to download the marked image.
- **Request Parameters:**
  - **image**: (file) The image file to be processed.
- **Query Parameters:**
  - **download**: (optional, boolean) If set to `true`, the API will return the image with detected objects marked. If `false` or not provided, it will return only the JSON response.
- **Response:**
  - **Content-Type:** `image/jpeg`
  - **Sample Usage:**
    - If the `download` parameter is set to `true`, the response will prompt the user to download the image file with detected objects marked.

### 3. API Documentation
- **Endpoint:** `/`
- **Method:** `GET`
- **Description:** Returns information on how to use the API.
- **Response:**
  - **Content-Type:** `text/html`
  - **Response:** A simple HTML page explaining how to use the API.


## Acknowledgements
- YOLO11 for object detection.
- Pillow for image processing.
- Flask for web framework.