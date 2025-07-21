from ultralytics import YOLO

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

# Load your trained YOLO11 model
model = YOLO("/Users/abundent/Documents/coding/Python/A-computer-vision/Udemy-CV/Computer_Vision_with_Python_Mazar/Object-Detection/runs/train/vehicles_yolo116/weights/best.pt")  # <-- Update with your best.pt path

# Run inference on your test image
results = model("/Users/abundent/Documents/coding/Python/A-computer-vision/Udemy-CV/Computer_Vision_with_Python_Mazar/Datasets/VehiclesDetection_Dataset/test/00dea1edf14f09ab_jpg.rf.KJ730oDTFPdXdJxvSLnX.jpg")  # <-- Update with your test image path

# Show the image with detections (will pop up a window)
results.show()

# Optionally, save the result to a file
results.save("results/")  # Saves to results directory

# Print the predictions
print(results[0].boxes)
