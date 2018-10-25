#!/usr/bin/python3
# -*- coding: utf-8 -*-


def main():
    end_of_input = [ list('.' * 8) for x in range(8)]
    gameCount = 0
    white = {
        "P": [(-1,-1),(1,-1)],
        "R": [(-1,-1),(1,-1),(-1,1),(1,1)],
        "N": [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)],
        "B": [(-1,-1),(1,-1),(1,1),(-1,1)],
        "Q": [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)],
        "K": [(-1,-1),(1,-1),(1,1),(-1,1),(-1,-1),(1,-1),(-1,1),(1,1)]
    }

    black = {
        "p": [(-1,1),(1,1)],
        "r": [(-1,-1),(1,-1),(-1,1),(1,1)],
        "n": [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)],
        "b": [(-1,-1),(1,-1),(1,1),(-1,1)],
        "q": [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)],
        "k": [(-1,-1),(1,-1),(1,1),(-1,1),(-1,-1),(1,-1),(-1,1),(1,1)]
    }


    config = getConfig(end_of_input)
    while config != end_of_input:
        # debug
        for row in config:
            for col in row:
                print(col, end="")
            print()

        # dictionaries for holding the coordinates of the pieces
        w_pieces = dict()
        b_pieces = dict()
        danger_zone = []

        gameCount += 1

        # traverses each cell in the matrix
        for row_index in range(len(config)):
            for col_index in range(len(config[0])):

                # constructs the dictionaries for white ang black
                curr_matrix_data = config[row_index][col_index]
                if curr_matrix_data.isalpha():
                    if curr_matrix_data.isupper():
                        if curr_matrix_data not in w_pieces:
                            w_pieces[curr_matrix_data] = [(col_index, row_index)]
                        else:
                            w_pieces[curr_matrix_data].append((col_index, row_index))
                    else:
                        if curr_matrix_data not in b_pieces:
                            b_pieces[curr_matrix_data] = [(col_index, row_index)]
                        else:
                            b_pieces[curr_matrix_data].append((col_index, row_index))
        if getDanger(config, w_pieces, white, b_pieces['k']):
            print("Game #" + str(gameCount) + ": black king is in check.")
        elif getDanger(config, b_pieces, black, w_pieces['K']):
            print("Game #" + str(gameCount) + ": white king is in check.")
        else:
            print("Game #" + str(gameCount) + ": no king is in check.")
        config = getConfig(end_of_input)


def getDanger(MATRIX, ALLY, AMOVES, ENEMY_KING):
    # print("king: ", ENEMY_KING)
    verdict = False
    danger_zone = []
    for piece in ALLY:
        loc_lower_piece = piece.lower()
        for coordinate in ALLY[piece]:
            if loc_lower_piece == 'p' or loc_lower_piece == 'n' or loc_lower_piece == 'k':
                for motion in AMOVES[piece]:
                    new_pos = (coordinate[0]+motion[0], coordinate[1]+motion[1])
                    if (0 <= new_pos[0] < 8) and (0 <= new_pos[1] < 8) and (new_pos[0], new_pos[1]) not in danger_zone:
                        if MATRIX[new_pos[1]][new_pos[0]] == "." or MATRIX[new_pos[1]][new_pos[0]].lower() == 'k':
                            danger_zone.append((coordinate[0]+motion[0], coordinate[1]+motion[1]))
            elif loc_lower_piece == 'r':
                for y in range(8):
                    if (coordinate[0],y) not in danger_zone:
                        if MATRIX[y][coordinate[0]] == '.' or MATRIX[y][coordinate[0]].lower() == 'k':
                            danger_zone.append((coordinate[0], y))
                        else:
                            break
                for x in range(8):
                    if (x,coordinate[1]) not in danger_zone:
                        if MATRIX[y][coordinate[0]] == '.' or MATRIX[y][coordinate[0]].lower() == 'k':
                            danger_zone.append((x, coordinate[1]))
                        else:
                            break
            elif loc_lower_piece == 'b':
                for motion in AMOVES[piece]:
                    currCoordinate = coordinate
                    while (0 <= currCoordinate[0]+motion[0] < 8) and (0 <= currCoordinate[1]+motion[1] < 8):
                        currCoordinate = (currCoordinate[0]+motion[0], currCoordinate[1]+motion[1])
                        if MATRIX[currCoordinate[1]][currCoordinate[0]] != '.' and MATRIX[currCoordinate[1]][currCoordinate[0]].lower() != 'k':
                            break
                        if currCoordinate not in danger_zone:
                            danger_zone.append(currCoordinate)
            elif loc_lower_piece == 'q':
                for y in range(8):
                    if (coordinate[0],y) not in danger_zone:
                        if MATRIX[y][coordinate[0]] == '.' or MATRIX[y][coordinate[0]].lower() == 'k':
                            danger_zone.append((coordinate[0], y))
                        else:
                            break
                for x in range(8):
                    if (x,coordinate[1]) not in danger_zone:
                        if MATRIX[y][coordinate[0]] == '.' or MATRIX[y][coordinate[0]].lower() == 'k':
                            danger_zone.append((x, coordinate[1]))
                        else:
                            break
                for motion in AMOVES[piece]:
                    currCoordinate = coordinate
                    while (0 <= currCoordinate[0]+motion[0] < 8) and (0 <= currCoordinate[1]+motion[1] < 8):
                        currCoordinate = (currCoordinate[0]+motion[0], currCoordinate[1]+motion[1])
                        if MATRIX[currCoordinate[1]][currCoordinate[0]] != '.' and MATRIX[currCoordinate[1]][currCoordinate[0]].lower() != 'k':
                            break
                        if currCoordinate not in danger_zone:
                            danger_zone.append(currCoordinate)
    print(ENEMY_KING, danger_zone)
    if ENEMY_KING[0] in danger_zone:
        verdict = True
    return verdict


def getConfig(END_OF_INPUT):
    locList = []
    for count in range(8):
        locList.append(list(input()))
    if locList != END_OF_INPUT:
        input() # skips the new line 
    return locList
        
def printMatrix(pMATRIX):
    for row in pMATRIX:
        for col in row:
            print(col, end='')
        print()


if __name__ == "__main__":
    main()
