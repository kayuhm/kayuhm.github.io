#!/usr/bin/python3

# determines if the sides can form a triangle

a = float(input())
b = float(input())
c = float(input())
classification = ""

if (a <= 0 or b <= 0 or c <= 0 or a + b <= c or b + c <= a or a + c <= b):
    print("INVALID")
else:
    if (a == b and b == c):
        classification = "EQUILATERAL"
    elif (a == b or a == c):
        classification = "ISOSCELES"
    else:
        classification = "SCALENE"

    print(classification + " TRIANGLE")
