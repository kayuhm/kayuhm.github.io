#!/usr/bin/python3

number = int(input())
length = 0

# check for length
if (number < 0):
    length = len(str(number)) - 1
else:
    length = len(str(number))

if (length <= 2):
    print("FALSE")
else:
    if (number % 2 == 0 or number % 3 == 0 or number % 5 == 0):
        print("TRUE")
    else:
        print("FALSE")
