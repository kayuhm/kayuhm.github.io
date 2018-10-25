#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    dictionary = []
    line = ""
    while True:
        line = input()
        if line == "X" * 6:
            break
        else:
            dictionary.append(line)

    scrambled = []
    while True:
        line = input()
        if line == "X" * 6:
            break
        else:
            scrambled.append(line)
            
    dictionary.sort()
    sortWord = ""
    finalList = []
    for word in scrambled:
        sortWord = ''.join(sorted(word))
        finalList.append([ text for text in dictionary if sortWord == ''.join(sorted(text)) ])
    # print(finalList)
    for results in finalList:
        if results:
            for content in results:
                print(content)
        else:
            print("NOT A VALID WORD")
        print("*" * 6)

if __name__ == "__main__":
    main()
