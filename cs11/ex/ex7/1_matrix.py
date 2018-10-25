#!/usr/bin/python3
# -*- coding: utf-8 -*-


def main():
    bin_op = {
        "row": row,
        "col": col,
    }

    un_op = {
        "inc": inc,
        "dec": dec,
        "transpose": transpose
    }

    t = int(input())
    case_count = 0
    while t != 0:
        matrix = []
        for count in range(int(input())):
            matrix.append([int(x) for x in list(input())])
        for count in range(int(input())):
            op_input = input().split(' ', 1)
            if len(op_input) == 1:
                matrix = un_op[op_input[0]](matrix)
            else:
                matrix = bin_op[op_input[0]](matrix, op_input[1])
        case_count += 1
        printMatrix(matrix, case_count)
        t -= 1


def printMatrix(MATRIX, CASE_COUNT):
        print("Case #" + str(CASE_COUNT))
        for matrix_row in MATRIX:
            for matrix_col in matrix_row:
                print(matrix_col, end="")
            print()
        print()


def row(MATRIX, LIST):
    loc_arg = [int(x) - 1 for x in LIST.split()]
    tmp = MATRIX[loc_arg[0]]
    MATRIX[loc_arg[0]] = MATRIX[loc_arg[1]]
    MATRIX[loc_arg[1]] = tmp
    return MATRIX


def col(MATRIX, LIST):
    loc_arg = [int(x) for x in LIST.split()]
    loc_a = loc_arg[0] - 1
    loc_b = loc_arg[1] - 1
    for index in range(len(MATRIX)):
        tmp = MATRIX[index][loc_a]
        MATRIX[index][loc_a] = MATRIX[index][loc_b]
        MATRIX[index][loc_b] = tmp
    return MATRIX


def inc(MATRIX):
    for index_row in range(len(MATRIX)):
        for index_col in range(len(MATRIX[0])):
            MATRIX[index_row][index_col] += 1
            if MATRIX[index_row][index_col] >= 10:
                MATRIX[index_row][index_col] %= 10
    return MATRIX


def dec(MATRIX):
    for index_row in range(len(MATRIX)):
        for index_col in range(len(MATRIX[0])):
            MATRIX[index_row][index_col] -= 1
            if MATRIX[index_row][index_col] <= 0:
                MATRIX[index_row][index_col] %= 10
    return MATRIX


def transpose(MATRIX):
    return [[matrix_row[index] for matrix_row in MATRIX] for index in range(len(MATRIX[0]))]



if __name__ == "__main__":
    main()
