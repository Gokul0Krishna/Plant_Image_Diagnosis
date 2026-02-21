import os
from dotenv import load_dotenv
from ultralytics import YOLO
import numpy as np

class Vision_model():
    def __init__(self):
        'An image classification YOLO model'
        load_dotenv()
        model_path = os.getenv('video_model_path')
        self.image_store = os.getenv('image_store_path')
        self.model = YOLO(model_path)

    def callasify(self,image) -> str:
        '''
        input: image
        output: the class to which the image has been classified to
        '''
        res = self.model(image)
        image = res[0]
        image.save(filename=self.image_store)
        detected_classes = []
        for box in image.boxes:
            cls_id = int(box.cls[0])
            class_name = image.names[cls_id]
            detected_classes.append(class_name)
        
        return detected_classes
        

if __name__ == '__main__':
    obj = Vision_model()
    print(obj.callasify(r"C:\Users\ASUS\Downloads\Plant Disease.v4i.yolo26\test\images\bercak_daun--522-_JPG.rf.f9c7d292a16ceecc2352956a940f452a.jpg"))