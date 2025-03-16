
import torch
from ultralytics import YOLO

def export_model(model_path='models/RBC_v10s.pt'):
    model = YOLO(model_path)
    model.export(format='onnx', opset=13, simplify=True)
    model.export(format='engine', half=True, workspace=16)
    print("Model exported successfully.")

if __name__ == "__main__":
    export_model()
