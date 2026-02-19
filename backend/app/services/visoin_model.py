import os
from dotenv import load_dotenv
from ultralytics import YOLO
import numpy as np
class Vision_model():
    def __init__(self):
        'An image classification YOLO model'
        load_dotenv()
        model_path = os.get_env('video_model_path')
        self.model = YOLO(model_path)
    def run(self,image) -> str:
        '''
        input: image
        output: the class to which the image has been classified to
        '''
        res = self.model(image)
        return res
