# server.py
import io
import torch
from fastapi import FastAPI, UploadFile, File, HTTPException
from torchvision import models, transforms
from PIL import Image
import uvicorn

app = FastAPI(title="Snap & Solve Guardrail Server")

# 1. Load the Model (CPU only to save resources)
print("Loading PyTorch ResNet18 Model...")
weights = models.ResNet18_Weights.DEFAULT
model = models.resnet18(weights=weights)
model.eval() # Set to inference mode

# 2. Setup Image Preprocessing
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# 3. Define "Academic" ImageNet Class IDs (e.g., Envelope, Menu, Web Site, Book Jacket)
# ImageNet has 1000 classes. We accept document-like classes.
# Added 530 (digital clock) and 531 (digital watch) just in case!
VALID_CLASSES = [921, 923, 931, 684, 504, 735, 916, 782, 664, 862, 527, 415, 922, 530, 531] 

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")

    try:
        image_bytes = await file.read()
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        batch_t = preprocess(img).unsqueeze(0)

        with torch.no_grad():
            out = model(batch_t)
        
        # Get the top prediction
        _, index = torch.max(out, 1)
        class_id = index.item()
        
        # Guardrail Logic
        is_academic = class_id in VALID_CLASSES
        category = weights.meta["categories"][class_id]

        return {
            "class_id": class_id,
            "category_name": category,
            "is_academic": is_academic,
            "confidence": "high"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Runs the server on port 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)