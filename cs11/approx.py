#!/usr/bin/python3

from sys import argv

x = float(argv[1])

expo_result = 1
factorial_result = 1
term_result = 1
final_result = 0

counter = 1 

while (0.000001 < term_result or term_result < -0.000001):
    # this goes first to make room for when x = 0
    term_result = expo_result / factorial_result
    final_result = final_result + term_result

    expo_result = expo_result  * x
    factorial_result = factorial_result * counter
    counter =  counter + 1


# output final_result
print(final_result)
