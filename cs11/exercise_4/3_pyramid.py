#!/usr/bin/python3

from math import ceil

def build():
    pass

def pyramid(dimension):
    width = dimension * 2 - 1
    total_width = width ** 2
    total_mid = ceil(total_width/2)
    counter = 0
    middles = [total_mid]

    for big_row in range(dimension):
        if big_row > 0:
            middles.append(total_mid - width * big_row)
            middles.append(total_mid + width * big_row)
            middles.sort()

        for row in range(dimension):
            for col in range(total_width):
                counter = 0
                for mid in middles:
                    if col < mid - 1 - row:
                        print(' ', end='')
                        break
                    elif col <= mid - 1 + row:
                        print('*', end='')
                        break
            print()

if __name__ == "__main__":
    pyramid(4)
