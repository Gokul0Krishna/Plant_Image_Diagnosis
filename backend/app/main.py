from fastapi import FastAPI, UploadFile, File
import os
from dotenv import load_dotenv
import requests

load_dotenv()
AIRFLOW_TRIGGER_URL = os.getenv('airflow_trigger_ur')

app = FastAPI()

UPLOAD_FOLDER = "uploaded_images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

 

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    requests.post(
        AIRFLOW_TRIGGER_URL,
        json={"conf": {"image_path": file_path}},
        auth=("airflow", "airflow")
    )
