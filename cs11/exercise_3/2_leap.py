#!/usr/bin/python3

y = int(input())

if (y < 1000):
    print("INPUT TOO SMALL")
else:
    if (y % 4 == 0):
        if (y % 100 == 0):
            if (y % 400 == 0):
                print("LEAP YEAR")
            else:
                print("NOT A LEAP YEAR")
        else:
            print("LEAP YEAR")
    else:
        print("NOT A LEAP YEAR")
