#!/usr/bin/python3

N = int(input())
sum_of_numbers = 0
sum_of_squares = 0

if (N <= 0):
    print("Invalid!!!")
else:
    sum_of_numbers = N * (N + 1) / 2
    sum_of_squares = N * (N + 1) * (2*N + 1) / 6
    print(int(sum_of_numbers * sum_of_numbers - sum_of_squares))
