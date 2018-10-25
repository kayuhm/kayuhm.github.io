#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    t = int(input())
    while t != 0:
        # turn the input into a single string
        sentence = ''.join(input().split()).lower()

        # get a set of unique letters in sentence
        unique = {letter for letter in sentence}

        # print(sentence)
        # print(unique)

        # make list for the unique letters
        # make a pair list of char count with letters[]
        letters = []
        count = []
        for char in unique:
            letters.append(char)
            count.append(sentence.count(char))

        # sorts the list by char count
        orderedPairs = sorted(zip(count, letters), reverse=True)

        # gets the ordered letters and count lists
        ordLetters = [ x[1] for x in orderedPairs ]
        ordCount = [ x[0] for x in orderedPairs ]

        # print(ordLetters)
        # print(ordCount)

        finalString = []
        locFinalString = []
        currCount = 0
        for index in range(len(ordCount)):
            currCount = ordCount[index]
            if index == len(ordCount) - 1:
                if ordCount[index] == ordCount[index-1]:
                    locFinalString.append(ordLetters[index])
                    finalString.append(locFinalString)
                else:
                    finalString.append(locFinalString)
                    finalString.append(ordLetters[index])
            elif currCount == ordCount[index+1]:
                locFinalString.append(ordLetters[index])
            else:
                locFinalString.append(ordLetters[index])
                finalString.append(locFinalString)
                locFinalString = []

        for group in finalString:
            print(''.join(sorted(group)), end="")
        print()
        # print(letters)
        # print(count)
        t -= 1

if __name__ == "__main__":
    main()
