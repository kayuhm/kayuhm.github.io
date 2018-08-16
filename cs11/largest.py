#!/usr/bin/python3

from sys import argv

# PARSING ARGUMENTS

n_size = int(argv[1])
n = []

# DEBUGGING
# print(n_size)
# print(n)

if (n_size >= 1):
    if (n_size == 1):
        print("Largest: " + str(argv[2]))
    else:
        for i in range(2, n_size + 2):
            n.append(argv[i])

        largest = n[0]
        counter = 1
        while (counter < n_size):
            if (largest < n[counter]):
                largest = n[counter]

            counter = counter + 1

        print("Largest: " + str(largest))
