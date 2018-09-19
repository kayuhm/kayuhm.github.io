#!/usr/bin/env env python3

def main():
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
    p_deg = int(P_POLY.pop(0))
    q_deg = int(Q_POLY.pop(0))
    p_len = len(P_POLY)
    q_len = len(Q_POLY)
    if (p_len > q_len):
        for i in range(p_len - q_len):
            print(str(P_POLY.pop(p_len - 1)) + "x^" + str(p_deg), end=" + ")
            p_len -= 1
            p_deg -= 1
    else:
        for i in range(q_len - p_len):
            print(str(Q_POLY.pop(q_len - 1)) + "x^" + str(q_deg), end=" ")
            q_len -= 1
            q_deg -= 1
    for index in range(p_len - 1, -1, -1):
        print(str(int(P_POLY[index]) + int(Q_POLY[index])) + "x^" + str(p_deg), end="")
        if p_deg != 0:
            print(" + ", end="")
        else:
            print()
        p_deg -= 1

if __name__ == "__main__":
    main()
