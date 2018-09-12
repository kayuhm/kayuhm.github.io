#!/usr/bin/python3

from math import ceil

def main():
    t = int(input())
    if t <= 0:
        pass # temporary
    else:
        # variable declarations
        array = []
        h = 0
        for i in range(t):
            h = int(input())
            if h <= 0:
                return
            else:
                array.append(h)

        for element in array:
            pyramid(element)

def pyramid(dimension):
    width = dimension * 2 - 1
    total_width = width ** 2
    total_mid = ceil(total_width / 2)
    middles = []
    center = dimension
    while center < total_width:
        middles.append(center)
        center = center + width

    for big_row in range(dimension):
        for row in range(dimension):
            for col in range(total_width):
                for center in middles:
                    if col < center - 1 - row:
                        print(' ', end='')
                    elif col <= center - 1 + row:
                        print('*', end='')
            print()

    # DEBUG
    print("width: " + str(width))
    print("total_width: " + str(total_width))
    print("total_mid: " + str(total_mid))
    print(middles)

if __name__ == "__main__":
    pyramid(2)
