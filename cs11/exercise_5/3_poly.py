#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    t = int(input())
    if t <= 0:
        # saved for error
        pass
    else:
        p = []
        q = []
        for i in range(t):
            p.append(input().split())
            q.append(input().split())
        for index in range(len(p)):
            poly(p[index], q[index])

def poly(Px, Qx):
    Px.pop(0)
    Qx.pop(0)
    p_len = len(Px)
    q_len = len(Qx)
    smaller = 0
    bigger = 0
    resList = []
    bool_lead = False

    if p_len == q_len:
        smaller = p_len
        bigger = q_len
    elif p_len > q_len:
        smaller = q_len
        bigger = p_len
    else:
        smaller = p_len
        bigger = q_len

    counter = 0 # while loop counter
    while counter < bigger:
        # this puts combines both polynomial lists into one
        # original order of polynomial array is retained
        # smaller degree - bigger degree [0, 1, 2, 3, ..., n]
        if counter < smaller:
            resList.append(int(Px.pop(0)) + int(Qx.pop(0)))
        else:
            if len(Px) > 0:
                for count in range(len(Px)):
                    resList.append(int(Px.pop(0)))
            else:
                for count in range(len(Qx)):
                    resList.append(int(Qx.pop(0)))
        counter += 1

    # for DEBUGGING PURPOSES
    # print(resList)

    degree = len(resList) - 1
    sign = ""
    for index in range(len(resList)-1, -1, -1):
        # for loop that will print the combined polynomial list
        if resList[index] == 0 and degree == 0 and not bool_lead:
                print("0x^0", end="")
        elif resList[index] != 0:
            if not bool_lead:
                print(str(resList[index]) + "x^" + str(degree), end="")
                bool_lead = True
            else:
                # modified from > ---> >=
                if (resList[index] > 0):
                    sign = "+"
                else:
                    sign = "-"
                print(" " + sign + " " + str(abs(resList[index])) + "x^" + str(degree), end="")

            degree -= 1
        else:
            degree -= 1
    print()

if __name__ == "__main__":
    main()
