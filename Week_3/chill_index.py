
print('1:')
# To calculate wind chill index.
# take inputs as temperaature, wind velocity
temp = int(input('Enter tempreture in ºF: '))
wind_vel = float(input('Enter wind velocity in mph: '))
wind_chill_index = round(35.74 + 0.6215 * temp - (35.75 * (wind_vel * 0.16)) + 0.4275 * (wind_vel * 0.16), 2)
# get output
print('Wind chill index:', wind_chill_index)

print('\n2:')
from math import pi, sin, cos, asin, ceil, floor

# convert radian to degree
# take inputs from user in radian
rad = float(input('Enter angle in radian: '))
deg = round(rad * (180 / pi), 2)
# get output
print('Angle in degree:', deg)

print('\n3:')
# To calculate distance between two points using latitude and longitude.
r = 6371
# take input from user as longitude and latitude of two points
lat_1 = float(input('Enter latitude of place 1: '))
lon_1 = float(input('Enter longitude of place 1: '))
lat_2 = float(input('Enter latitude of place 2: '))
lon_2 = float(input('Enter longitude of place 2: '))
# convert to radians
lon_1 = lon_1 * pi / 180
lon_2 = lon_2 * pi / 180
lat_1 = lat_1 * pi / 180
lat_2 = lat_2 * pi / 180
# FIND DISTANCE IN TERMS OF ANGLE
dlat = lat_2 - lat_1
dlon = lon_2 - lon_1
d1 = 2 * (dlat / 2) * 2 + cos(lat_1) * cos(lat_2) * sin(dlon / 2) * 2
# FIND DISTANCE
dis = round(2 * asin(d1 ** 0.5) * r, 2)
print('Distance between two places:', dis, 'km')

print('\n4:')
# To round the value of -4.3 and then takes the absolute value of that result.
num = -4.3
num = round(num, 0)
print('Rounded off number:', num)
print('Absolute value of rounded off number:', abs(num))

print('\n5:')
# program That takes the ceiling of sine of 34.5.
# use ceil function
print('Ceiling of sine(-4.3) is:', ceil(sin(-4.3)))

print('\n6:')
# Program To produce the floor of -2.8.
print('Floor of -2.8 is:', floor(-2.8))
