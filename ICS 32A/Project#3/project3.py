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
        center = geo.GeoForWeb()
        search = line1[17:]
    elif line1[:12] == 'CENTER FILE ':
        center = geo.GeoForFile()
        search = line1[12:]
    lat1, lon1 = center.get_forward_geo(search)

    if line5 == 'AQI PURPLEAIR':
        data = aqi.AqiDataWeb()
    elif line5[:9] == 'AQI FILE ':
        data = aqi.AqiDataFile(line5[9:])
    aqi_data = data.get_aqi_data()

    sensor_list = find_info(miles,min_aqi, max_num, aqi_data, lat1, lon1)
    sensor_list = aqi.sort_sensors(sensor_list)
    max_num = len(sensor_list)

    if max_num == 0:
        print(geo.print_center((lat1, lon1)))
        sys.exit()

    names = []
    if line6 == 'REVERSE NOMINATIM':
        for i in range(max_num):
            lat,lon = sensor_list[i].get_coordinates()
            names.append(geo.GeoRevWeb((lat,lon)))
    elif line6[:13] == 'REVERSE FILE ':
        path_list = line6[13:].split(' ')
        for i in range(max_num):
            names.append(geo.GeoRevFile(path_list[i]))             
    for i in range(max_num):
        text = names[i].get_reverse_geo()
        sensor_list[i].set_description(text)

    print(geo.print_center((lat1, lon1)))
    aqi.print_sensors(sensor_list)


if __name__ == '__main__':
    run()
