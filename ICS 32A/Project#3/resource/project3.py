# Eric Trinh / 20091235 / project3.py

import aqi
import geo

def find_info(distance: int, threshold: int, index: int, data: dict) -> [aqi.Sensor]:
    counter = 0
    sensor_list = []

    for sensor in data['data']:
        c1 = not(type(sensor[1]) == int or type(sensor[1]) == float)
        c2 = sensor[4] > 60
        c3 = sensor[25] == 1
        c4 = type(sensor[27]) != float
        c5 = type(sensor[28]) != float

        aqi = aqi.calculate_aqi(sensor[1])
        c6 =  aqi < threshold
##            distance??????

        if not(c1 or c2 or c3 or c4 or c5 or c6):
            sensor_list.append(aqi.Sensor(sensor[27],sensor[28],aqi))
            counter += 1
            
        if counter == index:
            break

    return sensor_list

def run() -> None:
    pass







if __name__ == '__main__':
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
        lat0, lon0 = retrieve_location()
        center = geo.Coordinate(lat,lon)
        lat1, lon1 = center.get_string_coordinates()
        print(f'CENTER {lat1} {lon1}')
    elif line1[:12] == 'CENTER FILE ':
        lat0, lon0 = retrieve_location_file(line1[12:])
        center = geo.Coordinate(lat,lon)
        lat1, lon1 = center.get_string_coordinates()
        print(f'CENTER {lat1} {lon1}')

    if line5 == 'AQI PURPLEAIR':
        aqi_data = retrieve_aqi()
    elif line5[:9] == 'AQI FILE ':
        aqi_data = retrieve_aqi_file(line5[9:])

    x = find_info(0,int(line3[10:]), int(line4[4:]), aqi_data)





        
    if line6 == 'REVERSE NOMINATIM':
        pass
    elif line6[:15] == 'REVERSE FILE ':
        pass
    


    
