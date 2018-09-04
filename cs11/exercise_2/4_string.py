#!/usr/bin/python3

str1 = input()
str2 = input()
N = int(input())

if (N < 0):
    print("Invalid!!!")
elif (N != 0):
    print((str1 + str2) * N)
