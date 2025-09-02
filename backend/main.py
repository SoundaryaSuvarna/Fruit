from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import shutil
import os

# Dummy fallback functions for now
def predict_image(path):
    return {"label": "dummy", "confidence": 1.0}

def predict_gas(mq135, mics5524, fruit):
    return {"freshness": "dummy", "score": 1.0}

app = FastAPI()
UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# CORS (for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict/image/")
async def image_predict(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = predict_image(file_location)
    return JSONResponse(content=result)

@app.post("/predict/gas/")
async def gas_predict(
    fruit: str = Form(...),
    mq135: float = Form(...),
    mics5524: float = Form(...)
):
    result = predict_gas(mq135, mics5524, fruit)
    return JSONResponse(content=result)

@app.get("/")
def root():
    return {"status": "API Running"}
