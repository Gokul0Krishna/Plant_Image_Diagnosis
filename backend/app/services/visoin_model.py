import os
from dotenv import load_dotenv
from ultralytics import YOLO
import numpy as np
class Vision_model():
    def __init__(self):
        'An image classification CNN model'
        load_dotenv()
        model_path = os.get_env('video_model_path')

    def run(self,image_array) -> str:
        '''
        input: array of the image
        output: the class to which the image has been classified to
        '''
        res = self.model.predict(image_array)
        return self.class_list[np.argmax(res)]
