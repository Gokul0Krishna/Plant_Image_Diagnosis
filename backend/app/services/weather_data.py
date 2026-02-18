import requests

class Weather_Data():

    def __init__(self):
        self.url = "https://api.open-meteo.com/v1/forecast"

    def _seven_days_past(self,loc:list):
        lat = float(loc[0])
        long = float(loc[1])
        past_days = 7
        params = {
        "latitude": lat,
        "longitude": long,
        "past_days": past_days 
        }
        response = requests.get(self.url, params=params)
        return response.json()

    def _seven_days_forcast(self,loc:list):
        lat = float(loc[0])
        long = float(loc[1])
        forecast_days = 7
        params = {
        "latitude": lat,
        "longitude": long,
        "forecast_days": forecast_days
        }
        response = requests.get(self.url, params=params)
        return response.json()
    
    def getdata(self,loc:list):
        past = self._seven_days_past(loc)
        future = self._seven_days_forcast(loc)
        return past,future

if __name__ == "__main__":
    obj = Weather_Data()
    print(obj.getdata())
