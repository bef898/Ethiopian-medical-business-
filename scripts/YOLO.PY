import torch
import os
import cv2
import pandas as pd

# Function to load YOLO model
def load_yolo_model():
    # Load the YOLO model (assuming YOLOv5 is installed and configured)
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    return model

# Function to run YOLO detection on images and save results + images
def run_yolo_detection(input_dir, output_dir, conf_threshold=0.4):
    model = load_yolo_model()

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List to hold detection results for each image
    detection_results = []

    image_files = [f for f in os.listdir(input_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        image_path = os.path.join(input_dir, image_file)

        # Run YOLO detection
        results = model(image_path, size=640)
        
        # Filter results by confidence threshold
        detection_data = results.pandas().xyxy[0]
        detection_data = detection_data[detection_data['confidence'] >= conf_threshold]

        if not detection_data.empty:
            detection_data['image_name'] = image_file  # Add image name to the detection data
            detection_results.append(detection_data)  # Append the detection data for the image

            # Open image with OpenCV
            img = cv2.imread(image_path)
            
            # Draw bounding boxes and labels
            for i, row in detection_data.iterrows():
                xmin, ymin, xmax, ymax = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
                label = f"{row['name']} {row['confidence']:.2f}"
                
                # Draw bounding box and label
                cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)  # Bounding box
                cv2.putText(img, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

            # Save the annotated image to the output folder
            output_image_path = os.path.join(output_dir, image_file)
            cv2.imwrite(output_image_path, img)

    # Return combined detection results as a DataFrame
    return pd.concat(detection_results, ignore_index=True) if detection_results else pd.DataFrame()
