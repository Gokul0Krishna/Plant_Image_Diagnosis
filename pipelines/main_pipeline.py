import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prefect import task, flow
from backend.app.services import Loc_api,Weather_Data,Filter_my_data,Vision_model,Llm

@task
def Get_weather():
    obj1 = Loc_api()
    obj2 = Weather_Data()
    filt = Filter_my_data()
    loc = obj1.getloc()
    past,future = obj2.getdata(loc=loc)
    past_data = filt.filter(past)
    future_data = filt.filter(future)
    return past_data,future_data

@task
def Image_process(Image_path):
    obj = Vision_model()
    return obj.callasify(image=Image_path)

@task
def Llm_use(img_class,pdata,fdata): 
    obj = Llm()
    return obj.run(pdata=pdata,fdata=fdata,plant_class=img_class)
@flow
def main_line(image_path):
    img_class = Image_process(image_path)
    pdata,fdata = Get_weather()
    print(img_class)
    print(pdata)
    print(fdata)
    result = Llm_use(img_class=img_class,pdata=pdata,fdata=fdata)
    return result

if __name__ == '__main__':
    print(main_line(image_path=r"C:\Users\ASUS\Downloads\Plant Disease.v4i.yolo26\test\images\bercak_daun--522-_JPG.rf.f9c7d292a16ceecc2352956a940f452a.jpg"))