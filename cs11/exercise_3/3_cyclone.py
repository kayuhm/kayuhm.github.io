#!/usr/bin/python3

wind_speed = float(input())
classification = ""

if (wind_speed <= 61):
    classification = "TROPICAL DEPRESSION"
elif (wind_speed <= 88):
    classification = "TROPICAL STORM"
elif (wind_speed <= 117):
    classification = "SEVERE TROPICAL STORM"
elif (wind_speed <= 220):
    classification = "TYPHOON"
else:
    classification = "SUPER TYPHOON"

print(classification)
