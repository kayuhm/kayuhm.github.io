#!/usr/bin/python3

from sys import argv

n = int(argv[1])

prev = 0
curr = 1
fib = 0

# the iteration begins from 3rd fib (fib[2])
counter = 2

if (n >= 0):
    print(prev)

    if (n > 0):
        print(curr)

        while (n >= counter):
            fib = prev + curr
            prev = curr
            curr = fib
            print(fib)
            counter += 1
