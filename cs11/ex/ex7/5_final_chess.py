#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    end_config = [['.' for x in range(8)] for y in range(8)]
    game_count = 0
    config = getConfig()
    while config != end_config:
        game_count += 1
        print("Game #" + str(game_count) + ": ", end="")
        print(checkForCheck(config))
        config = getConfig()

def getConfig():
    loc_matrix = []
    for count in range(8):
        loc_matrix.append(list(input()))
    try:
        input() # removes excess space
    except EOFError:
        pass
    return loc_matrix


def checkForCheck(pMATRIX):
    # suppose to print( black/white king is in check.)
    w_check = "white king is in check."
    b_check = "black king is in check."
    for row_index in range(len(pMATRIX)):
        for col_index in range(len(pMATRIX[0])):
            if pMATRIX[row_index][col_index] == 'p':
                try:
                    if pMATRIX[row_index+1][col_index-1] == 'K' or pMATRIX[row_index+1][col_index+1] == 'K':
                        return w_check
                except IndexError:
                    pass
            elif pMATRIX[row_index][col_index] == 'P':
                try:
                    if pMATRIX[row_index-1][col_index-1] == 'k' or pMATRIX[row_index-1][col_index+1] == 'k':
                        return b_check
                except IndexError:
                    break
            elif pMATRIX[row_index][col_index].lower() == 'n':
                loc_motion = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
                for motion in loc_motion:
                    cur_coord = (col_index+motion[0], row_index+motion[1])
                    if cur_coord[0] < 0 or cur_coord[1] < 0:
                        continue
                    try:
                        if pMATRIX[cur_coord[1]][cur_coord[0]] == 'K' and pMATRIX[row_index][col_index] == 'n':
                            return w_check
                        elif pMATRIX[cur_coord[1]][cur_coord[0]] == 'k' and pMATRIX[row_index][col_index] == 'N':
                            return b_check
                    except IndexError:
                        continue
            elif pMATRIX[row_index][col_index].lower() == 'r':
                loc_motion = [(-1,0),(0,-1),(1,0),(0,1)]
                for motion in loc_motion:
                    cur_coord = (col_index, row_index)
                    while True:
                        try:
                            cur_coord = (cur_coord[0]+motion[0], cur_coord[1]+motion[1])
                            if cur_coord[0] < 0 or cur_coord[1] < 0:
                                break
                            if pMATRIX[cur_coord[1]][cur_coord[0]] != '.':
                                if pMATRIX[cur_coord[1]][cur_coord[0]] == 'K' and pMATRIX[row_index][col_index] == 'r':
                                    return w_check
                                elif pMATRIX[cur_coord[1]][cur_coord[0]] == 'k' and pMATRIX[row_index][col_index] == 'R':
                                    return b_check
                                else:
                                    break
                        except IndexError:
                            break
            elif pMATRIX[row_index][col_index].lower() == 'b':
                loc_motion = [(-1,-1),(1,-1),(1,1),(-1,1)]
                for motion in loc_motion:
                    cur_coord = (col_index, row_index)
                    while True:
                        try:
                            cur_coord = (cur_coord[0]+motion[0], cur_coord[1]+motion[1])
                            if cur_coord[0] < 0 or cur_coord[1] < 0:
                                break
                            if pMATRIX[cur_coord[1]][cur_coord[0]] != '.':
                                if pMATRIX[cur_coord[1]][cur_coord[0]] == 'K' and pMATRIX[row_index][col_index] == 'b':
                                    return w_check
                                elif pMATRIX[cur_coord[1]][cur_coord[0]] == 'k' and pMATRIX[row_index][col_index] == 'B':
                                    return b_check
                                else:
                                    break
                        except IndexError:
                            break
            elif pMATRIX[row_index][col_index].lower() == 'q':
                loc_motion = [(-1,0),(0,-1),(1,0),(0,1)]
                for motion in loc_motion:
                    cur_coord = (col_index, row_index)
                    while True:
                        try:
                            cur_coord = (cur_coord[0]+motion[0], cur_coord[1]+motion[1])
                            if cur_coord[0] < 0 or cur_coord[1] < 0:
                                break
                            if pMATRIX[cur_coord[1]][cur_coord[0]] != '.':
                                if pMATRIX[cur_coord[1]][cur_coord[0]] == 'K' and pMATRIX[row_index][col_index] == 'q':
                                    return w_check
                                elif pMATRIX[cur_coord[1]][cur_coord[0]] == 'k' and pMATRIX[row_index][col_index] == 'Q':
                                    return b_check
                                else:
                                    break
                        except IndexError:
                            break
                loc_motion = [(-1,-1),(1,-1),(1,1),(-1,1)]
                for motion in loc_motion:
                    cur_coord = (col_index, row_index)
                    while True:
                        try:
                            cur_coord = (cur_coord[0]+motion[0], cur_coord[1]+motion[1])
                            if cur_coord[0] < 0 or cur_coord[1] < 0:
                                break
                            if pMATRIX[cur_coord[1]][cur_coord[0]] != '.':
                                if pMATRIX[cur_coord[1]][cur_coord[0]] == 'K' and pMATRIX[row_index][col_index] == 'q':
                                    return w_check
                                elif pMATRIX[cur_coord[1]][cur_coord[0]] == 'k' and pMATRIX[row_index][col_index] == 'Q':
                                    return b_check
                                else:
                                    break
                        except IndexError:
                            break
    return "no king is in check."


def printMatrix(pMATRIX):
    for row in pMATRIX:
        for col in row:
            print(col, end="")
        print()

if __name__ == "__main__":
    main()
