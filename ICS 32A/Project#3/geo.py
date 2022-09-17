# Eric Trinh / 20091235 / geo.py

from pathlib import Path
import urllib.parse
import urllib.request
import json
import math
import sys


class GeoForWeb():
    def get_forward_geo(self, search: str) -> tuple:
        try:
            base_url = 'https://nominatim.openstreetmap.org/search?'
            form = '&format=json&limit=1'
            query = urllib.parse.urlencode([('q',search)])
            url = base_url + query + form
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


class GeoForFile():
    def get_forward_geo(self, search: str):
        try:
            file_path = Path(search)
            file = file_path.open('r', encoding = 'utf-8')
            json_text = file.read()
            data = json.loads(json_text)[0] 
            return float(data['lat']),float(data['lon'])
        except FileNotFoundError:
            print(f'FAILED\n{search}\nMISSING')
            sys.exit()
        except:
            print(f'FAILED\n{search}\nFORMAT')
            sys.exit()


class GeoRevWeb():
    def __init__(self, point: tuple):
        self._lat, self._lon = str(point[0]), str(point[1])
    def get_reverse_geo(self) -> str:
        try:
            base_url = 'https://nominatim.openstreetmap.org/reverse?'
            form = '&format=json&limit=1'
            query = urllib.parse.urlencode([('lat',self._lat),('lon',self._lon)])
            url = base_url + query + form
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


class GeoRevFile():
    def __init__(self, link: str):
        self._path = link
    def get_reverse_geo(self) -> str:
        try:
            file_path = Path(self._path)
            file = file_path.open('r', encoding = 'utf-8')
            json_text = file.read()
            data = json.loads(json_text)
            return data['display_name']
        except FileNotFoundError:
            print(f'FAILED\n{self._path}\nMISSING')
            sys.exit()
        except:
            print(f'FAILED\n{self._path}\nFORMAT')
            sys.exit()


def print_center(point: tuple) -> str:
    '''
    Given a tuple containing the latitude and longitude,
    prints the coordinates with the directions added
    '''
    if point[0] < 0:
        lat = str(point[0]*-1) + '/S'
    else:
        lat = str(point[0]) + '/N'
    if point[1] < 0:
        lon = str(point[1]*-1) + '/W'
    else:
        lon = str(point[1]) + '/E'
    return f'CENTER {lat} {lon}'


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
