from airflow import DAG
from datetime import datetime
import json
from backend.app.services.image_transform import Image_processing
from backend.app.services.visoin_model import Vision_model

def load_and_process(**context):
    pass
