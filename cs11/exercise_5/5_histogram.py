#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    t = int(input())
    b = []
    data = []
    for count in range(t):
        b.append(int(input()))
        data.append(input().split())
    for index in range(len(b)):
        hist(b[index], data[index])

def hist(BIN_SIZE, DATA_LIST):
    locBinSizeOffset = BIN_SIZE - 1
    locDataList = []
    locLowerBound = 0
    locHigherBound = 0
    frequency = 0
    counter = 0

    # converts all items in DATA_LIST into type 'int'
    for element in DATA_LIST:
        locDataList.append(int(element))

    locDataList.sort()
    locLowerBound = locDataList[0]
    locHigherBound = locLowerBound + locBinSizeOffset


    # ouputs the frequency table
    while counter < len(locDataList):
        # print("lower: " + str(locLowerBound))
        # print("higher: " + str(locHigherBound))
        # print("value: " + str(locDataList[counter]))
        if locLowerBound <= locDataList[counter] <= locHigherBound:
            frequency += 1
            counter += 1
            if counter == len(locDataList):
                print(str(locLowerBound) + "-" + str(locHigherBound), frequency)
        else:
            print(str(locLowerBound) + "-" + str(locHigherBound), frequency)
            locLowerBound = locHigherBound + 1
            locHigherBound = locLowerBound + locBinSizeOffset
            frequency = 0
    print() # add line break before next set of outputs



if __name__ == "__main__":
    main()
