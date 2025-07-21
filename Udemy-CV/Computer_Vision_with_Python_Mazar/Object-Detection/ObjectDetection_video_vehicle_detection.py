from ultralytics import YOLO
import os

"""
# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train on your dataset
results = model.train(
    data="/Users/abundent/Documents/coding/Python/A-computer-vision/Udemy-CV/Computer_Vision_with_Python_Mazar/Datasets/VehiclesDetection_Dataset/dataset.yaml",
    epochs=6,
    imgsz=640,
    batch=8,
    project="runs/train",
    name="vehicles_yolo11"
)
"""

## Inference (testing ) the trained Model
from ultralytics import YOLO

# Load your trained YOLO model
model = YOLO("/Users/abundent/Documents/coding/Python/A-computer-vision/Udemy-CV/Computer_Vision_with_Python_Mazar/Object-Detection/runs/train/vehicles_yolo116/weights/best.pt")

# Path to test (can be a file or a folder)
test_path = "/Users/abundent/Documents/coding/Python/A-computer-vision/Udemy-CV/Computer_Vision_with_Python_Mazar/Datasets/VehiclesDetection_Dataset/test/images/00dea1edf14f09ab_jpg.rf.KJ730oDTFPdXdJxvSLnX.jpg"
output_dir = "results/"
os.makedirs(output_dir, exist_ok=True)

def run_inference(image_path, output_dir, idx=0):
    results = model(image_path)
    for i, result in enumerate(results):
        result.show()
        output_path = os.path.join(output_dir, f"result_{idx+i}.jpg")
        result.save(output_path)
        print(result.boxes)

if os.path.isdir(test_path):
    image_files = [os.path.join(test_path, f) for f in os.listdir(test_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    for idx, image_file in enumerate(image_files):
        run_inference(image_file, output_dir, idx)
else:
    run_inference(test_path, output_dir)
