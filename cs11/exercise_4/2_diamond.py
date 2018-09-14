#!/usr/bin/python3

def main():
    t = int(input())
    if t > 0:
        # variable declarations
        array = []
        s = 0
        for i in range(t):
            s = int(input())
            if s <= 0:
                return
            else:
                array.append(s)

        for element in array:
            diamond(element)

def diamond(side):
    length = side * 2 - 1
    for i in range(side):
        for j in range(length):
            if (j < side - 1 - i):
                print(' ', end='')
            elif (j <= side - 1 + i):
                print('*', end='')
            else:
                break
        print()
    for i in range(side - 2, -1, -1):
        for j in range(length):
            if (j < side - 1 - i):
                print(' ', end='')
            elif (j <= side - 1 + i):
                print('*', end='')
            else:
                break
        print()
    print() # separates diamonds





if __name__ == "__main__":
    main()
