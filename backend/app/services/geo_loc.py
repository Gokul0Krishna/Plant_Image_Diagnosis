import requests

class Loc_api():

    def __init__(self):
        'uses requests library that returns latitude longitude'
        pass

    def getloc(self) -> list:
        '''
        input: nothing
        output: list containing latititude and longitude
        '''
        response = requests.get('https://ipinfo.io/')
        data = response.json()
        loc = data.get('loc', '').split(',')
        return loc


if __name__ == '__main__':
    obj = Loc_api()
    obj.getloc()