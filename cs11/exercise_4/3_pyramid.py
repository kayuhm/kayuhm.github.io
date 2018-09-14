#!/usr/bin/python3

def main():
    t = int(input())
    if t > 0:
        # variable declarations
        array = []
        h = 0
        for i in range(t):
            h = int(input())
            if h <= 0:
                return
            else:
                array.append(h)

        for element in array:
            pyramid(element)

# THIS IS THE ULTRA EASY PYTHON WAY
def pyramid(dimension):
    for big_row in range(dimension):
        for row in range(dimension):
            print((' ' * (dimension * 2 - 1) * (dimension - big_row - 1)), end='')
            for col in range(2 * big_row + 1):
                print((' ' * (dimension - row - 1)), end='')
                print('*' * (2 * row + 1), end='')
                if (col != 2*big_row):
                    print(' ' * (dimension - row - 1), end='')
            print()
    print() 

# THIS IS THE LOW-LEVEL (C PROGRAMMING) STYLE OF SOLUTION
# def pyramid(dimension):
#     width = dimension * 2 - 1
#     total_width = width ** 2
#     total_mid = ceil(total_width/2)
#     counter = 0
#     middles = [total_mid]
#
#     for big_row in range(dimension):
#         if big_row > 0:
#             middles.append(total_mid - width * big_row)
#             middles.append(total_mid + width * big_row)
#             middles.sort()
#
#         for row in range(dimension):
#             for col in range(total_width):
#                 counter = 0
#                 for mid in middles:
#                     if col < mid - 1 - row:
#                         print(' ', end='')
#                         break
#                     elif col <= mid - 1 + row:
#                         print('*', end='')
#                         break
#             print()
#     print()

if __name__ == "__main__":
    main()
