#!/usr/bin/env env python3


t = int(input())
if t <= 0:
    # saved for invalid input output
    pass
else:
    arrPx = []
    arrQx = []
    for i in range(t):
        arrPx.append(input().split())
        arrQx.append(input().split())

    for i in range(len(arrPx)):
        polyAdd(arrPx[i], arrQx[i])

def polyAdd(P_POLY, Q_POLY):
    difference = 0
    biggest = 0
    if len(P_POLY) > len(Q_POLY):
        biggest = len(P_POLY)
        difference = biggest - len(Q_POLY) - 1
        for i in range(1, difference + 1):
            print(str(P_POLY[i]) + "x^" + str(P_POLY[0]))
            P_POLY[0] -= 1
    else:
        biggest = len(Q_POLY)
        difference = biggest - len(P_POLY) - 1
        for i in range(1, difference + 1):
            print(str(Q_POLY[i]) + "x^" + str(Q_POLY[0]))
            Q_POLY[0] -= 1
    for index in range(difference + 1, ):


if __name__ == "__main__":
    main()
