import os
from dotenv import load_dotenv
from ultralytics import YOLO
import numpy as np
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parents[3]  

class Vision_model():
    def __init__(self):
        'An image classification YOLO model'
        # env_path = BASE_DIR / ".env"
        load_dotenv()
        model_path = os.getenv('video_model_path')
        self.image_store = os.getenv('image_store_path')
        print(model_path)
        # model_path = r'C:\Users\ASUS\OneDrive\Desktop\private\backend\app\model\best (1).pt'
        self.model = YOLO(model_path)

    def callasify(self,image) -> str:
        '''
        input: image
        output: the class to which the image has been classified to
        '''
        res = self.model(image)
        image = res[0]
        if os.path.exists(self.image_store):
            os.remove(self.image_store)
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