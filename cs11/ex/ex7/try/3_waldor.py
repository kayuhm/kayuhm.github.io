#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    t = int(input())
    offsets = [(x,y) for x in range(-1,2) for y in range(-1,2) if (x,y) != (0,0)]
    # print(offsets)
    while t != 0:
        input()
        dimensions = [int(x) for x in input().split()]
        matrix = [[char for char in input()] for count in range(dimensions[0])]
        # lower all upper in matrix
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[0])):
                if matrix[row_index][col_index].isupper():
                    matrix[row_index][col_index] = matrix[row_index][col_index].lower()

        words_to_find = []
        for count in range(int(input())):
            words_to_find.append(input())
        for word in words_to_find:
            # lowers word
            lowerWord = word.lower()
            for row_index in range(len(matrix)):
                for col_index in range(len(matrix[0])):
                    # start search in matrix
                    verdict = False
                    if matrix[row_index][col_index] == lowerWord[0] and len(lowerWord) != 1:
                        # if a letter on the matrix matches the first letter of the word, start checking all possible directions
                        for motion in offsets:
                            verdict = True
                            cur_row = row_index
                            cur_col = col_index
                            for char_index in range(1, len(lowerWord)):
                                cur_col += motion[0]
                                cur_row += motion[1]
                                # print("col", cur_col, "row", cur_row)
                                # print(matrix[cur_row][cur_col], "=", word[char_index], motion, cur_col + 1, cur_row + 1)
                                # print()
                                try:
                                    if matrix[cur_row][cur_col] != lowerWord[char_index] or cur_col < 0 or cur_col >= len(matrix[0]) or cur_row < 0 or cur_row >= len(matrix):
                                        # if next char is not equal to char then break
                                        # breaks word iterator
                                        verdict = False
                                        break
                                except IndexError:
                                    pass
                                if verdict and char_index == len(lowerWord) - 1:
                                    print(row_index+1, col_index+1)
                                    break # breaks for char_index in range(1, len(lowerWord))
                            if verdict == True:
                                break # breaks for motion in offsets
                    elif matrix[row_index][col_index] == lowerWord[0] and len(lowerWord) == 1:
                        verdict = True 
                        print(row_index+1, col_index+1)

                    if verdict == True:
                        break # breaks for col_index in range()
                if verdict == True:
                    break # breaks for row_index in range()

        if t != 1:
            print()
        
        # prints matrix for error checking
        # print(' ', end="")
        # for count in range(1,len(matrix[0]) + 1):
        #     print(" ", end="")
        #     print(count, end="")
        # print()
        # for rowChar in range(len(matrix)):
        #     print(str(rowChar + 1) + ' ', end="")
        #     for colChar in range(len(matrix[rowChar])):
        #         print(matrix[rowChar][colChar] + " ", end="")
        #     print()
        t -= 1


if __name__ == "__main__":
    main()
