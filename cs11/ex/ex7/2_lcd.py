#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    line = input()
    while line != "0 0":
        displayLCD(line)
        line = input()


def displayLCD(pNumStr):
    pNumStr = pNumStr.split()
    pNumStr[0] = int(pNumStr[0])
    s = pNumStr[0]
    # hor = '\u2588'
    # ver = '\u2588'

    hor = '-'
    ver = '|'

    # traits
    traits = {
        # reference: 0 1 2 3 4 5 6 7 8 9
        # top/bottom (0=none, 1=exists)
        # mid (0=none, 1=exists)
        # top_side/bot_side (0=left only, 1=right only, 2=both)
        "top": [1,0,1,1,0,1,1,1,1,1],
        "top_side": [2,1,1,1,2,0,0,1,2,2],
        "mid": [0,0,1,1,1,1,1,0,1,1],
        "bot_side": [2,1,0,1,1,1,2,1,2,1],
        "bot": [1,0,1,1,0,1,1,0,1,1],
    }

    # top
    for index in range(len(pNumStr[1])):
        print(' ', end="")
        if (traits["top"][int(pNumStr[1][index])]) == 0:
            print(' ' * s, end="")
        else:
            print(hor * s, end="")
        print(' ', end="")
        if index != len(pNumStr[1]) - 1:
            print(' ', end="")
    print()

    # top_side
    for count in range(s):
        for index in range(len(pNumStr[1])):
            if traits["top_side"][int(pNumStr[1][index])] == 0 or traits["top_side"][int(pNumStr[1][index])] == 2:
                print(ver, end="")
            else:
                print(' ', end="")
            print(' ' * s, end="")
            if traits["top_side"][int(pNumStr[1][index])] == 1 or traits["top_side"][int(pNumStr[1][index])] == 2:
                print(ver, end="")
            else:
                print(' ', end="") 
            if index != len(pNumStr[1]) - 1:
                print(' ', end="")
        print()

    # mid
    for index in range(len(pNumStr[1])):
        print(' ', end="")
        if (traits["mid"][int(pNumStr[1][index])]) == 0:
            print(' ' * s, end="")
        else:
            print(hor * s, end="")
        print(' ', end="")
        if index != len(pNumStr[1]) - 1:
                print(' ', end="")
    print()

    # bot_side
    for count in range(s):
        for index in range(len(pNumStr[1])):
            if traits["bot_side"][int(pNumStr[1][index])] == 0 or traits["bot_side"][int(pNumStr[1][index])] == 2:
                print(ver, end="")
            else:
                print(' ', end="")
            print(' ' * s, end="")
            if traits["bot_side"][int(pNumStr[1][index])] == 1 or traits["bot_side"][int(pNumStr[1][index])] == 2:
                print(ver, end="")
            else:
                print(' ', end="") 
            if index != len(pNumStr[1]) - 1:
                print(' ', end="")
        print()

    # bottom
    for index in range(len(pNumStr[1])):
        print(' ', end="")
        if (traits["bot"][int(pNumStr[1][index])]) == 0:
            print(' ' * s, end="")
        else:
            print(hor * s, end="")
        print(' ', end="")
        if index != len(pNumStr[1]) - 1:
            print(' ', end="")
    print('\n')


if __name__ == "__main__":
    main()
