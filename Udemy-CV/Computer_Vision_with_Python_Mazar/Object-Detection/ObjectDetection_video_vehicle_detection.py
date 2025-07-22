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

# --- IMAGE OR FOLDER INFERENCE ---
# Uncomment and set test_path to run image/folder inference
# test_path = "/Users/abundent/Documents/coding/Python/A-computer-vision/Udemy-CV/Computer_Vision_with_Python_Mazar/Datasets/VehiclesDetection_Dataset/test/images/"  # folder
test_path = "/Users/abundent/Documents/coding/Python/A-computer-vision/Udemy-CV/Computer_Vision_with_Python_Mazar/Datasets/VehiclesDetection_Dataset/test/images/00dea1edf14f09ab_jpg.rf.KJ730oDTFPdXdJxvSLnX.jpg"  # single image

output_dir = "results/"
os.makedirs(output_dir, exist_ok=True)

def run_inference(image_path, output_dir, idx=0):
    results = model(image_path)
    for i, result in enumerate(results):
        result.show()
        output_path = os.path.join(output_dir, f"result_{idx+i}.jpg")
        result.save(output_path)
        print(result.boxes)

# Uncomment below to run image/folder inference
if 'test_path' in locals():
     if os.path.isdir(test_path):
         image_files = [os.path.join(test_path, f) for f in os.listdir(test_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
         for idx, image_file in enumerate(image_files):
             run_inference(image_file, output_dir, idx)
     else:
         run_inference(test_path, output_dir)

# --- VIDEO INFERENCE ---
video_test_path = "/Users/abundent/Documents/coding/Python/A-computer-vision/Udemy-CV/Computer_Vision_with_Python_Mazar/Datasets/VehiclesDetection_Dataset/TrafficPolice.mp4"
video_output_dir = "results/video/"
os.makedirs(video_output_dir, exist_ok=True)

def run_video_inference(video_path, output_dir):
    print(f"Starting video inference on: {video_path}")
    results = model(video_path, save=True, project=output_dir, name="video_results", verbose=True)
    # Find the actual output video file
    output_folder = os.path.join(output_dir, "video_results")
    video_basename = os.path.splitext(os.path.basename(video_path))[0]
    output_video_path = os.path.join(output_folder, f"{video_basename}_predict.mp4")
    # Log number of frames processed if available
    if hasattr(results, '__len__'):
        print(f"Frames processed: {len(results)}")
    else:
        print("Frame count not available in results object.")
    # List output folder contents
    print(f"Output folder contents: {os.listdir(output_folder) if os.path.exists(output_folder) else 'Folder not found'}")
    if os.path.exists(output_video_path):
        print(f"Processed video saved at: {output_video_path}")
    else:
        print(f"Processed video folder: {output_folder}. Check for output files.")
    print("Video inference completed.")

# Uncomment below to run video inference
#run_video_inference(video_test_path, video_output_dir)



# evaluating the model 
# metrics = model.val()
# saving the model  as coreml
model.export(format='coreml', dynamic=False, imgsz=640)