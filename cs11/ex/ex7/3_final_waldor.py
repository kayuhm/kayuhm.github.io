#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    t = int(input())
    input() # skips empty space in input
    while t != 0:
        matrix = getMatrix()
        words = getWords()
        locate(matrix, words)
        if t != 1:
            print()
        t -= 1


def locate(pMATRIX, pWORDS):
    directions = [(-1,-0),(0,-1),(1,0),(0,1),(-1,-1),(1,-1),(1,1),(-1,1)]
    for word in pWORDS:
        verdict = False
        for row_index in range(len(pMATRIX)):
            if verdict:
                break
            for col_index in range(len(pMATRIX[0])):
                if verdict:
                    break
                if pMATRIX[row_index][col_index] == word[0]:
                    if len(word) == 1:
                        print(row_index+1, col_index+1)
                        verdict = True
                        break
                    else:
                        for motion in directions:
                            if verdict:
                                break
                            curr_coord = (col_index+motion[0], row_index+motion[1])
                            if curr_coord[0] < 0 or curr_coord[1] < 0:
                                continue
                            try:
                                if pMATRIX[curr_coord[1]][curr_coord[0]] == word[1]:
                                    if len(word) == 2:
                                        print(row_index+1, col_index+1)
                                        # print(row_index+1, col_index+1)
                                        verdict = True
                                        break
                                    else:
                                        for word_index in range(2, len(word)):
                                            try:
                                                curr_coord = (curr_coord[0]+motion[0], curr_coord[1]+motion[1])
                                                if curr_coord[0] < 0 or curr_coord[1] < 0:
                                                    break
                                                if pMATRIX[curr_coord[1]][curr_coord[0]] != word[word_index]:
                                                    break
                                            except IndexError:
                                                break
                                            if word_index == len(word) - 1:
                                                print(row_index+1, col_index+1)
                                                verdict = True
                                                break
                            except IndexError:
                                continue


def getMatrix():
    loc_dimensions = input().split()
    loc_matrix = []
    for count in range(int(loc_dimensions[0])):
        loc_matrix.append(list(input().lower()))
    return loc_matrix


def getWords():
    loc_words = []
    for count in range(int(input())):
        loc_words.append(input().lower())
    try:
        input() # skips empty space
    except EOFError:
        pass
    return loc_words


def printMatrix(pMATRIX):
    for row in pMATRIX:
        for col in row:
            print(col + ' ', end="")
        print()


if __name__ == "__main__":
    main()
