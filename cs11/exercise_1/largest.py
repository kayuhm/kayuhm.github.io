#!/usr/bin/python3

from sys import argv

counter = 2

n_size = int(input("Number of Elements: "))
input_number = 0
largest = int(input("1: "))

while (counter <= n_size):
    input_number = int(input(str(counter) + ": "))
    if (largest < input_number):
        largest = input_number
    counter = counter + 1

print("Largest: " + str(largest))
