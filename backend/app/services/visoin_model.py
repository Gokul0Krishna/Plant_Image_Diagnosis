import os
from dotenv import load_dotenv
from tensorflow.keras import layers, models
import numpy as np
class Vision_model():
    def __init__(self):
        
        'An image classification CNN model'

        load_dotenv()
        video_model_path = os.getenv('video_model_path')
        self.model = models.Sequential([
                                            layers.Conv2D(32,(3,3),activation='relu',input_shape=(244,244,3)),
                                            layers.MaxPooling2D(2,2),

                                            layers.Conv2D(64,(3,3),activation='relu'),
                                            layers.MaxPooling2D(2,2),

                                            layers.Flatten(),
                                            layers.Dense(64,activation='relu'),
                                            layers.Dense(38,activation='softmax')   # number of classes
                                        ])
        self.model.load_weights(video_model_path)
        self.model.compile(
                            optimizer='adam',
                            loss='categorical_crossentropy',
                            metrics=['accuracy']
                        )
        
        self.class_list = ['Pepper,_bell___healthy', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Grape___Esca_(Black_Measles)', 'Apple___Black_rot',
                            'Tomato___Leaf_Mold', 'Tomato___Target_Spot', 'Tomato___Tomato_mosaic_virus', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                            'Strawberry___healthy', 'Cherry_(including_sour)___healthy', 'Potato___Late_blight', 'Grape___Black_rot', 'Apple___Apple_scab',
                            'Peach___Bacterial_spot', 'Squash___Powdery_mildew', 'Orange___Haunglongbing_(Citrus_greening)', 'Tomato___Early_blight', 
                            'Cherry_(including_sour)___Powdery_mildew', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                            'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Northern_Leaf_Blight', 'Grape___healthy', 
                            'Raspberry___healthy', 'Pepper,_bell___Bacterial_spot', 'Tomato___Late_blight', 'Apple___Cedar_apple_rust',
                            'Tomato___Bacterial_spot', 'Strawberry___Leaf_scorch', 'Potato___Early_blight', 'Tomato___healthy', 'Apple___healthy', 
                            'Soybean___healthy', 'Corn_(maize)___healthy', 'Tomato___Septoria_leaf_spot', 'Blueberry___healthy', 'Potato___healthy', 
                            'Peach___healthy', 'Corn_(maize)___Common_rust_'] 

    def run(self,image_array) -> str:
        '''
        input: array of the image
        output: the class to which the image has been classified to
        '''
        res = self.model.predict(image_array)
        return self.class_list[np.argmax(res)]
