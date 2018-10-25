#!/usr/bin/python3

from math import sqrt

a = int(input())
b = int(input())
c = int(input())

discriminant = b**2 - 4*a*c

if (discriminant < 0):
    print("No real solution.")
else:
    root1 = ((-b) + sqrt(b**2 - 4*a*c)) / 2*a
    root2 = ((-b) - sqrt(b**2 - 4*a*c)) / 2*a

    if (root2 < root1):
        print(round(root2, 2))
        print(round(root1, 2))
    else:
        print(round(root1, 2))
        print(round(root2, 2))

