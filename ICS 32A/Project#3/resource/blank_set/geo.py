# Eric Trinh / 20091235 / geo.py

from pathlib import Path
import urllib.parse
import urllib.request
import json
import math
import sys

class GeoData():
    pass


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


def retrieve_location(search: str) -> tuple:
    '''
    Given a string of a search, retrieves the JSON file
    for the corresponding search from NOMINATIM's Web
    API and returns a tuple containing the coordinates.
    '''
    try:
        url = forward_url(search)
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
        data = json.loads(json_text)[0]
        return float(data['lat']),float(data['lon'])
    except:
        print(f'FAILED\n{response.status} {url}\nFORMAT')
        sys.exit()


def retrieve_location_file(path: str) -> tuple:
    '''
    Given a string of a path, retrieves the JSON file
    from the corresponding directory and returns a
    tuple containing the coordinates
    '''
    try:
        file_path = Path(path)
        file = file_path.open('r', encoding = 'utf-8')
        json_text = file.read()
        data = json.loads(json_text)[0] 
        return float(data['lat']),float(data['lon'])
    except FileNotFoundError:
        print(f'FAILED\n{path}\nMISSING')
        sys.exit()
    except:
        print(f'FAILED\n{path}\nFORMAT')
        sys.exit()


def reverse_location(point: tuple) -> str:
    '''
    Given a tuple containing the latitude and longitude,
    retrieves the display name of the location from NOMINATIM's
    Web API and returns the string
    '''
    try:
        lat, lon = str(point[0]), str(point[1])
        url = reverse_url((lat, lon))
        
        url = 'https://www.youtube.com/asdfdsfasdfasfs'
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
        return data['display_name']
    except:
        print(f'FAILED\n{response.status} {url}\nFORMAT')
        sys.exit()


def reverse_location_file(path: str) -> str:
    '''
    Given a string of a path, retrieves the JSON file
    from the corresponding directory and returns the
    the display name of the location
    '''
    try:
        file_path = Path(path)
        file = file_path.open('r', encoding = 'utf-8')
        json_text = file.read()
        data = json.loads(json_text)
        return data['display_name']
    except FileNotFoundError:
        print(f'FAILED\n{path}\nMISSING')
        sys.exit()
    except:
        print(f'FAILED\n{path}\nFORMAT')
        sys.exit()


def get_distance(location: tuple, sensor: tuple) -> float:
    '''
    Given two tuples containing latitudes and longitudes,
    returns the distance of the two coordinates
    '''
    r = 3958.8
    dlat = (abs(location[0]) - abs(sensor[0])) * math.pi / 180
    dlon = (abs(location[1]) - abs(sensor[1])) * math.pi / 180
    alat = ((location[0] + sensor[0]) / 2) * math.pi / 180
    x = dlon * math.cos(alat)
    d = math.sqrt((x*x) + (dlat*dlat)) * r
    return d


def forward_url(search: str) -> str:
    '''
    Given a string of the search, returns the encoded
    search url for forward geocoding
    '''
    base_url = 'https://nominatim.openstreetmap.org/search?'
    form = '&format=json&limit=1'
    query = urllib.parse.urlencode([('q',search)])
    url = base_url + query + form
    return url


def reverse_url(point: tuple) -> str:
    '''
    Given a tuple containing a latitude and longitude,
    returns the encoded search url for reverse geocoding
    '''
    base_url = 'https://nominatim.openstreetmap.org/reverse?'
    form = '&format=json&limit=1'
    query = urllib.parse.urlencode([('lat',point[0]),('lon',point[1])])
    url = base_url + query + form
    return url
