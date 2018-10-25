#!/usr/bin/python3
# -*- coding: utf-8 -*

from math import ceil
from collections import Counter

def main():
    t = int(input())
    if t <= 0:
        pass
    else:
        arrInput = []
        for i in range(t):
            arrInput.append(int(input()))
        for element in arrInput:
            canonicalPrime(element) 

def canonicalPrime(N):
    factor = 2
    limit = ceil(N / 2)
    arr_factors = []
    while (True):
        if N % factor == 0:
            arr_factors.append(factor)
            N = N / factor
            factor = 1
        if factor > limit:
            if N != 1:
                arr_factors.append(int(N))
            break
        factor += 1
    arr_factors.sort()
    # print(arr_factors)
    curr = ""
    count = 0
    curr = arr_factors[0]
    for index in range(len(arr_factors)):
        if arr_factors[index]  == curr:
            count += 1
        else:
            print("(" + str(curr) + "^" + str(count) + ")", end="")
            curr = arr_factors[index]
            count = 1

        if index == len(arr_factors) - 1:
            print("(" + str(curr) + "^" + str(count) + ")", end="")
    print()


if __name__ == "__main__":
  main()

