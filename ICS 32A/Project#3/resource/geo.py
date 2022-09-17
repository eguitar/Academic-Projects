# Eric Trinh / 20091235 / geo.py

from pathlib import Path
import urllib.parse
import urllib.request
import json
import math

class Coordinate():
    def __init__(self, lat: float, lon: float):
        self._lat = lat
        self._lon = lon

    def get_coordinates(self) -> tuple:
        return self._lat, self._lon

    def get_string_coordinates(self) -> tuple:
        if self._lat < 0:
            _lat = str(self._lat*-1) + '/S'
        else :
            _lat = str(self._lat) + '/N'
        if self._lon < 0:
            _lon = str(self._lon*-1) + '/W'
        else :
            _lon = str(self._lon) + '/E'
        return _lat, _lon


def get_distance(location: tuple, sensor: tuple) -> float:
    r = 3958.8
    dlat = location[0] - sensor[0]
    dlon = location[1] - sensor[1]
    alat = (location[0] + sensor[0]) / 2
    x = dlon * math.cos(alat)
    d = math.sqrt(x*x + dlat*dlat) * r
    return d


def retrieve_location(search: str) -> tuple:
    base_url = 'https://nominatim.openstreetmap.org/search?'
    form = '&format=json&limit=1'
    query = urllib.parse.urlencode([('q',search)])
    url = base_url + query + form
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    json_text = response.read().decode(encoding = 'utf-8')
    data = json.loads(json_text)[0]
    return data['lat'],data['lon']

    
def retrieve_location_file(path: str) -> tuple:
    file_path = Path(path)
    file = file_path.open('r', encoding = 'utf-8')
    json_text = file.read()
    data = json.loads(json_text)[0] 
    return data['lat'],data['lon']


def reverse_location(point: tuple) -> str:
    lat, lon = str(point[0]), str(point[1])
    base_url = 'https://nominatim.openstreetmap.org/reverse?'
    form = '&format=json&limit=1'
    query = urllib.parse.urlencode([('lat',lat),('lon',lon)])
    url = base_url + query + form
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    json_text = response.read().decode(encoding = 'utf-8')
    data = json.loads(json_text)
    return data['display_name']


def reverse_location_file():
    pass
