#!/usr/bin/python3

from sys import argv

x = float(argv[1])

counter = 0
local_counter = 0

expo_result = float(0)
factorial_result = float(0)
final_result = float(0)
term_result = float(1)

while (0.000001 < term_result or 
term_result < 
-0.000001):
    # solve for exponential result
    # reinitialize local_counter to 0
    local_counter = 0
    expo_result = float(1)

    if (counter > 0):
        while (local_counter < 
counter):
            expo_result = expo_result * x
            local_counter = local_counter + 1

    # DEBUGGING
    # print("exponential result = " + str(expo_result))

    # solve for factorial
    # reinitialize local_counter to the value of x
    local__counter = x
    factorial_result = 1
    while (local_counter > 1):
        factorial_result = factorial_result * local_counter
        local_counter = local_counter - 1

    # DEBUGGING
    # print("factorial result = " + str(factorial_result))

    term_result = float(expo_result / factorial_result)
    final_result = final_result + term_result
    counter =  counter + 1


# output final_result
print(final_result)
