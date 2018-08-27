#!/usr/bin/python3

from sys import argv

N = argv[1]

if (int(N) >= 0):
    result = 0

    while (len(N) > 1):
        result = 0
        for element in str(N):
            result = result + int(element)
            N = str(result)

    print(N)
