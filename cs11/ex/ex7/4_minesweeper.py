#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    dimension = []
    row_size = 0
    col_size = 0
    safe_char = '.'
    bomb_char = '*'
    directions = [(x,y) for x in range(-1,2) for y in range(-1,2) if (x,y) != (0,0)]
    dimension = input()
    input_count = 1
    while True:
        row_size = dimension.split()
        col_size = int(row_size[1])
        row_size = int(row_size[0])
        matrix = []
        for count in range(row_size):
            matrix.append(list(input()))
        matrix = setClues(matrix, directions, safe_char, bomb_char)
        print("Field #" + str(input_count) + ':')
        printMatrix(matrix)
        dimension = input()
        input_count += 1
        if dimension == "0 0":
            break
        else:
            print()

def setClues(pMATRIX, pDIRECTIONS, pSAFE, pBOMB):
    for row_index in range(len(pMATRIX)):
        for col_index in range(len(pMATRIX[0])):
            count = 0
            if pMATRIX[row_index][col_index] == pSAFE:
                for motion in pDIRECTIONS:
                    try:
                        new_row = row_index + motion[1]
                        new_col = col_index + motion[0]
                        if (new_row >= 0 and new_col >= 0):
                            if pMATRIX[new_row][new_col] == pBOMB:
                                count += 1
                                # print(motion, count)
                                # print(col_index, row_index)
                                # print(col_index + motion[1], row_index + motion[0])
                    except IndexError:
                        continue
                pMATRIX[row_index][col_index] = count
    return pMATRIX



def printMatrix(pMATRIX):
    for row in pMATRIX:
        for col in row:
            print(col, end="")
        print()


if __name__ == "__main__":
    main()
