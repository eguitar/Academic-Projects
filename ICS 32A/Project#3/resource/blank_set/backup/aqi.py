# Eric Trinh / 20091235 / aqi.py

from pathlib import Path
import urllib.request
import json
import sys

class AqiData():
    def __init__(self):
        self._data = {}


class Sensor():
    def __init__(self, lat: float, lon: float, aqi: int):
        self._description = ''
        self._lat = lat
        self._lon = lon
        self._aqi = aqi
        
    def set_description(self, text: str):
        self._description = text

    def get_description(self):
        return self._description

    def get_coordinates(self):
        return self._lat, self._lon

    def get_aqi(self):
        return self._aqi

    def get_string_coordinates(self):
        if self._lat < 0:
            _lat = str(self._lat*-1) + '/S'
        else :
            _lat = str(self._lat) + '/N'
        if self._lon < 0:
            _lon = str(self._lon*-1) + '/W'
        else :
            _lon = str(self._lon) + '/E'
        return _lat, _lon



def retrieve_aqi() -> dict:
    '''
    Retrieves data in the form of a JSON file from
    NOMINATIM's Web API and returns it as a dictionary
    '''
    try:
        url = 'https://www.purpleair.com/data.json'
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        if response.status != 200:
            print(f'FAILED\n{response.status} {url}\nNOT 200')
            sys.exit()
    except urllib.error.HTTPError as e:
        print(f'FAILED\n{e.code} {url}\nNOT 200')
        sys.exit()
    except:
        print(f'FAILED\n{url}\nNETWORK')
        sys.exit()
    try:
        json_text = response.read().decode(encoding = 'utf-8')
        data = json.loads(json_text)
        return data
    except:
        print(f'FAILED\n{response.status} {url}\nFORMAT')
        sys.exit()


def retrieve_aqi_file(path: str) -> dict:
    '''
    Retrieves data in the form of a JSON file from
    a file on the comp given as path in a string
    and returns it as a dictionary
    '''
    try:
        file_path = Path(path)
        file = file_path.open('r', encoding = 'utf-8')
        json_text = file.read()
        data = json.loads(json_text)
        return data
    except FileNotFoundError:
        print(f'FAILED\n{path}\nMISSING')
        sys.exit()
    except:
        print(f'FAILED\n{path}\nFORMAT')
        sys.exit()


def calculate_aqi(pm: float) -> int:
    '''
    Given a float that represents the concentration
    of PM2.5, returns the AQI as an integer
    '''
    aqi = 0
    if pm >= 500.5:
        aqi = 501
    elif pm >= 350.5:
        scalar = (500 - 401) / (500.4 - 350.5)
        aqi = ((pm - 350.5) * scalar) + 401
    elif pm >= 250.5:
        scalar = (400 - 301) / (350.4 - 250.5)
        aqi = ((pm - 250.5) * scalar) + 301
    elif pm >= 150.5:
        scalar = (300 - 201) / (250.4 - 150.5)
        aqi = ((pm - 150.5) * scalar) + 201
    elif pm >= 55.5:
        scalar = (200 - 151) / (150.4 - 55.5)
        aqi = ((pm - 55.5) * scalar) + 151
    elif pm >= 35.5:
        scalar = (150 - 101) / (55.4 - 35.5)
        aqi = ((pm - 35.5) * scalar) + 101
    elif pm >= 12.1:
        scalar = (100 - 51) / (35.4 - 12.1)
        aqi = ((pm - 12.1) * scalar) + 51
    else:
        scalar = 50/12.0
        aqi = pm * scalar
    return round(aqi)


def sort_sensors(sensors: [Sensor]) -> [Sensor]:
    '''
    Given a list of Sensor objects, returns a sorted
    list in descending order based on the AQI value
    '''
    new_list = []
    order = {}
    counter = 0
    for sensor in sensors:
        order[sensor.get_aqi()] = counter
        counter += 1
    aqi_list = sorted(order.keys(),reverse = True)
    for aqi in aqi_list:
        index = order[aqi]
        new_list.append(sensors[index])
    return new_list
