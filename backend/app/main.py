import os
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles

load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel
from pipelines import main_line

app = FastAPI()

class ImagePathRequest(BaseModel):
    file_path: str

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.mount(
    "/images",
    StaticFiles(directory="backend/app/img"), 
    name="images"
)


@app.post("/upload-image")
async def upload_image(request: ImagePathRequest):
    result = main_line(request.file_path)
    return {
        "status": "success",
        "pipeline_output": result,
        "image_url": "/images/result.jpg"
    }

