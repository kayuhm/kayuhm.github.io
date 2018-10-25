#!/usr/bin/python3


# signum function definition
def sgn(x):
    result = 0
    if (x < 0):
        result = -1
    elif (x > 0):
        result = 1

    return result

print(sgn(float(input())))
