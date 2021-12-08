import math
from typing import Text

temp_input = 0.0
temp_scale = ''  # metric or english
wind_input = 0.0
wind_scale = ''  # metric or english
temp_C = 0.0
temp_F = 0.0
wind_english = 0.0
wind_metric = 0.0
calc_scale = ''  # metric or english
chill = 0.0


def convert_C_to_F(degree):
    temp_F = (1.8*degree)+32
    return temp_F


def convert_F_to_C(degree):
    temp_C = (degree-32)/1.8
    return temp_C


def metric_wind_to_english(speed):
    mph = 0.6213711922*speed
    return mph


def english_wind_to_metric(speed):
    kmph = speed/0.6213711922
    return kmph


def windchill(scale='english', temp=0.0, windspeed=0.0):
    scale = scale.lower()
    temp = float(temp)
    windspeed = float(windspeed)
    if scale == 'english':
        wc_factor = 35.74 + (0.6215*temp)-(35.75*(windspeed**0.16)
                                           ) + (0.4275*temp*(windspeed**0.16))
    elif scale == 'metric':
        temp = float(temp)
        windspeed = float(windspeed)
        wc_factor = 13.12 + (0.6215*temp)-(11.34*(windspeed**0.16)
                                           ) + (0.3965*temp*(windspeed**0.16))
    else:
        print('error error error does not compute')
    return wc_factor


print('How cold do you feel? ')
print('We are calculating the wind chill factor, today. ')
temp_input = float(input('What is the temperature outside? '))
temp_scale = input('Fahrenheit or Celcius (F/C)? ').upper()
if temp_scale == 'C':
    temp_C = temp_input
    temp_F = convert_C_to_F(temp_input)
else:
    temp_C = convert_F_to_C(temp_input)
    temp_F = temp_input
#print(f'That is {temp_F:.2f} F and {temp_C:.2f} C')

print('For the wind speed, will you be using metric (kmph) or English (mph) measurements?')
wind_scale = input('Enter "metric" or "English": ').lower()
wind_input = float(input('What is the wind speed? '))
if wind_scale == 'metric':
    wind_metric = wind_input
    wind_english = metric_wind_to_english(wind_input)
else:
    wind_metric = english_wind_to_metric(wind_input)
    wind_english = wind_input
#print(f'That is {wind_english:.2f} mph and {wind_metric:.2f} kmph.')

chill_e = windchill('english', temp_F, wind_english)
chill_me = windchill('metric', temp_C, wind_english)

print()
print(
    f'It feels like {chill_e:.2f}{chr(176)}F, or {chill_me:.2f}{chr(176)}C. ')
print()
print(
    f'Here is the Wind Chill Factor, with winds of {wind_english:.2f} mph ({wind_metric:.2f} kmph), over a range of temperatures: ')
for i in range(0, 65, 5):
    chill_e = windchill('english', i, wind_english)
    chill_me = windchill('metric', convert_F_to_C(i), wind_metric)
    print(
        f'At {i:.2f}{chr(176)}F ({convert_F_to_C(i):.2f}{chr(176)}C), with winds of {wind_english:.2f} mph ({wind_metric:.2f} kmph) it feels like {chill_e:.2f}{chr(176)}F ({chill_me:.2f}{chr(176)}C). ')
print()
print('So long, and thanks for all the fish. ')
print()
