# backend/main.py
import numpy as np
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
import io
import os
import time

from backend.utils.preprocessing import preprocess_image
from backend.utils.model_loader import load_trained_model

app = FastAPI()

# --- CORS ALLOWANCE ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all (or specify ["http://localhost:3000"] for safer option)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = load_trained_model()

@app.post("/predict/")
async def predict_digit(file: UploadFile = File(...)):
    content = await file.read()
    img = Image.open(io.BytesIO(content))

    # --- Save the uploaded image ---
    save_dir = "backend/debug_uploads"
    os.makedirs(save_dir, exist_ok=True)
    filename = f"upload_{int(time.time() * 1000)}.png"
    img.save(os.path.join(save_dir, filename))
    print(f"[✔] Saved uploaded image as {filename}")
    
    processed_img = preprocess_image(img)

    # --- Save the actual preprocessed image for debug ---
    processed_visual = Image.fromarray((processed_img.reshape(28, 28) * 255).astype(np.uint8))
    filename = f"after_upload_{int(time.time() * 1000)}.png"
    processed_visual.save(os.path.join(save_dir, filename))
    
    output = model.forward(processed_img)
    prediction = int(output.argmax())

    return JSONResponse(content={"prediction": prediction})
