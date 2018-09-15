#!/usr/bin/python3

sumOfFib = 2
fib = 0
curr = 2
prev = 1
while (True):
    fib = prev + curr
    prev = curr
    curr = fib
    if (fib > 4000000):
        break
    if (fib % 2 == 0):
        sumOfFib += fib
print(sumOfFib)
