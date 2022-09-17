# Eric Trinh / 20091235 / project3.py

import aqi
import geo
import sys

def find_info(distance: int, threshold: int, index: int,
              data: dict, lat: float, lon: float) -> [aqi.Sensor]:
    '''
    Given the max range in miles, the minimum AQI threshold, the
    max number of locations, the dictionary containing sensor
    information, and the latitude and longitude of the center,
    returns a list of n Sensor objects that comply with the input
    '''
    counter = 0
    sensor_list = []
    for sensor in data['data']:
        try:
            c1 = type(sensor[1]) != float
            c2 = sensor[4] > 60
            c3 = sensor[25] == 1
            c4 = type(sensor[27]) != float
            c5 = type(sensor[28]) != float
            level = aqi.calculate_aqi(sensor[1])
            c6 = level < threshold
            point = (sensor[27],sensor[28])
            c7 = geo.get_distance((lat,lon),point) > distance
            if not(c1 or c2 or c3 or c4 or c5 or c6 or c7):
                s = aqi.Sensor(sensor[27],sensor[28],level)
                sensor_list.append(s)
                counter += 1
            if counter == index:
                break
        except:
            pass
    return sensor_list


def print_sensors(sensor_list: [aqi.Sensor]) -> None:
    '''
    Given a list of Sensor objects, prints the AQI,
    the latitude and longitude, and the description
    of the location in separate lines
    '''
    for sensor in sensor_list:
        print(f'AQI {sensor.get_aqi()}')
        lat, lon = sensor.get_string_coordinates()
        print(f'{lat} {lon}')
        print(f'{sensor.get_description()}')


def run() -> None:
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    line5 = input()
    line6 = input()

    miles = int(line2[6:])
    min_aqi = int(line3[10:])
    max_num = int(line4[4:])

    if line1[:17] == 'CENTER NOMINATIM ':
        lat0, lon0 = geo.retrieve_location(line1[17:])
        center = geo.Coordinate(lat0,lon0)
        lat1, lon1 = center.get_string_coordinates()
        center_location = f'CENTER {lat1} {lon1}'
    elif line1[:12] == 'CENTER FILE ':
        lat0, lon0 = geo.retrieve_location_file(line1[12:])
        center = geo.Coordinate(lat0,lon0)
        lat1, lon1 = center.get_string_coordinates()
        center_location = f'CENTER {lat1} {lon1}'

    if line5 == 'AQI PURPLEAIR':
        aqi_data = aqi.retrieve_aqi()
    elif line5[:9] == 'AQI FILE ':
        aqi_data = aqi.retrieve_aqi_file(line5[9:])

    sensor_list = find_info(miles,min_aqi, max_num, aqi_data, lat0, lon0)
    sensor_list = aqi.sort_sensors(sensor_list)
    max_num = len(sensor_list)

    if max_num == 0:
        print(center_location)
        sys.exit()
    
    if line6 == 'REVERSE NOMINATIM':
        for i in range(max_num):
            lat,lon = sensor_list[i].get_coordinates()
            text = geo.reverse_location((lat,lon))
            sensor_list[i].set_description(text) 
    elif line6[:13] == 'REVERSE FILE ':
        path_list = line6[13:].split(' ')
        for i in range(max_num):
            text = geo.reverse_location_file(path_list[i])
            sensor_list[i].set_description(text)
    print(center_location)
    print_sensors(sensor_list)


if __name__ == '__main__':
    run()
