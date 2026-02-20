from prefect import task, flow
from backend.app.services import Loc_api,Weather_Data

@task
def get_weather():
    obj1 = Loc_api()
    obj2 = Weather_Data()
    loc = obj1.getloc()
    past,future = obj2.getdata(loc=loc)
    print(past,future)



@flow
def main_line():
    get_weather()

if __name__ == '__main__':
    main_line()