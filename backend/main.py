import numpy as np
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
import io

from utils.preprocessing import preprocess_image
from utils.model_loader import load_trained_model

app = FastAPI()

# --- CORS ALLOWANCE ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model once at startup
model = load_trained_model()

@app.post("/predict/")
async def predict_digit(file: UploadFile = File(...)):
    content = await file.read()
    img = Image.open(io.BytesIO(content))

    # Preprocess the image (convert to 28x28 grayscale)
    processed_img = preprocess_image(img)

    # Make prediction
    output = model.forward(processed_img)
    prediction = int(output.argmax())

    return JSONResponse(content={"prediction": prediction})
