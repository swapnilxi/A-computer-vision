from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from PIL import Image
import io
import uvicorn


app = FastAPI()

# Load your trained YOLO model once at startup
model = YOLO("path/to/best.pt")  # <-- put your best.pt path here

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read image data from the uploaded file
    image_bytes = await file.read()
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # Run YOLO inference
    results = model(img)
    # Results object contains predictions; let's format output
    pred_boxes = []
    for box in results[0].boxes:
        pred = {
            "class": int(box.cls),
            "confidence": float(box.conf),
            "box": [float(x) for x in box.xyxy[0]]
        }
        pred_boxes.append(pred)

    return {"predictions": pred_boxes}
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)