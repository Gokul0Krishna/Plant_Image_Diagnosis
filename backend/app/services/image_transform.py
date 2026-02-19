import pandas as pd
import numpy as np
from PIL import Image


class Image_processing():
    def __init__(self):

        'converts raw image to an array'
        
        pass

    def run(file_path:str) -> np.array:

        ''' input: file_path a string
            returns: an array of the image
        '''
        
        image = Image.open(file_path).convert('RGB')
        reimage = image.resize((244,244))
        image_array = np.array(reimage,dtype=np.float32)
        image_array = image_array/255.0
        return image_array
