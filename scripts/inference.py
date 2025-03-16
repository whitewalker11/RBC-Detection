import torch
import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLOv10 model
model = YOLO('models/RBC_V10s.pt')

def detect_rbc(image_path):
    """Runs RBC detection on a given image."""
    image = cv2.imread(image_path)
    results = model.predict(image)
    
    # Process results
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0].item()
            
            # Draw bounding box
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, f'RBC: {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Save output
    output_path = image_path.replace(".jpg", "_detected.jpg")
    cv2.imwrite(output_path, image)
    print(f"Detection complete. Saved at {output_path}")

# Example usage
detect_rbc('data/sample_image.jpg')