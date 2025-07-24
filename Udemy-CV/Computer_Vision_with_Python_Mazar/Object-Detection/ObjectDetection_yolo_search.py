from ultralytics import YOLO
import cv2
"""
# Specify your image path here
image_path = '/Users/abundent/Documents/coding/Python/A-computer-vision/Udemy-CV/Computer_Vision_with_Python_Mazar/Datasets/balloon_dataset/train/53500107_d24b11b3c2_b.jpg '

model = YOLO("yolo11n.pt")

# Read the image
image = cv2.imread(image_path)

# Run YOLO object detection
results = model(image)

# Plot (annotate) the results on the image
annotated_image = results[0].plot()
# the default was giving "baloon" as "apple" in result 

# Display the annotated image
cv2.imshow('YOLO Detection', annotated_image)
cv2.waitKey(0)  # Waits for any key press
cv2.destroyAllWindows()
"""

# Training the model
from ultralytics import YOLO

# Use yolov8, or substitute 'yolov11s.pt' if the model exists and is supported
model = YOLO("yolo11n.pt") # change to 'yolov11n.pt' if you have it

# Train the model
model.train(
    data='/Users/abundent/Documents/coding/Python/A-computer-vision/Udemy-CV/Computer_Vision_with_Python_Mazar/Datasets/balloon_dataset/balloon.yaml',
    epochs=5,  # adjust as needed
    imgsz=640   # or your preferred size
)

