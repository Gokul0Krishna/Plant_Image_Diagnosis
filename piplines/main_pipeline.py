import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prefect import task, flow
from backend.app.services import Loc_api,Weather_Data,Filter_my_data


@task
def get_weather():
    obj1 = Loc_api()
    obj2 = Weather_Data()
    filt = Filter_my_data()
    loc = obj1.getloc()
    past,future = obj2.getdata(loc=loc)
    past_data = filt.filter(past)
    future_data = filt.filter(future)
    print(past_data,future_data)



@flow
def main_line():
    get_weather()

if __name__ == '__main__':
    main_line()