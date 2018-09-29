#!/usr/bin/env python3
# -*- coding: utf-8 -*-


str1 = input()
str2 = input()
N = int(input())

if (N < 0):
    print("Invalid!!!")
elif (N != 0):
    print((str1 + str2) * N)
