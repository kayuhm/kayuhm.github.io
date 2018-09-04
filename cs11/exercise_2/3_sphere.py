#!/usr/bin/python3

from math import pi

radius = float(input())

if (radius <= 0):
    print("Invalid!!!")
else:
    vol_cube = (radius * 2) ** 3
    vol_sphere = 4 / 3 * pi * (radius**3)
    vol_around_sphere = vol_cube - vol_sphere
    print(round(vol_around_sphere, 4))
