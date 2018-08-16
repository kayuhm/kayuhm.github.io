#!/usr/bin/python3

from sys import argv

N = int(argv[1])

counter = 2
local_counter = 0
decision = "" # or not_prime

while counter < N:
    local_counter = 2
    decision = "prime"
    # print(counter)
    while (local_counter <= counter/2):
        if (counter % local_counter == 0):
            decision = "not_prime"
            local_counter = local_counter + 1
            break
        else:
            local_counter = local_counter + 1

    if (decision == "prime"):
        print(counter)

    counter = counter + 1
