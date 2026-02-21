import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prefect import task, flow
from backend.app.services import Loc_api,Weather_Data,Filter_my_data,Vision_model


@task
def get_weather():
    obj1 = Loc_api()
    obj2 = Weather_Data()
    filt = Filter_my_data()
    loc = obj1.getloc()
    past,future = obj2.getdata(loc=loc)
    past_data = filt.filter(past)
    future_data = filt.filter(future)
    return past_data,future_data

@task
def image_process(Image_path):
    obj = Vision_model()
    return obj.callasify(image=Image_path)


@flow
def main_line(image_path):
    img_class = image_process(image_path)
    pdata,fdata = get_weather()

if __name__ == '__main__':
    main_line()