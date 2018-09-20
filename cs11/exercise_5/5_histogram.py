#!/usr/bin/env python3

def main():
    t = int(input())
    if t <= 0:
        # saved for error
        pass
    else:
        b = []
        data = []
        for count in range(t):
            b.append(int(input()))
            data.append(input().split())
        for index in range(len(b)):
            hist(b[index], data[index])
         

def hist(BIN_SIZE, DATA_LIST):
    # make all data in DATA_LIST an int
    counter = 0
    while counter < len(DATA_LIST):
        DATA_LIST[counter] = int(DATA_LIST[counter])
        counter += 1
    DATA_LIST.sort()
    locBinSizeOffset = int(BIN_SIZE) - 1
    locLowerBound = [DATA_LIST[0]]
    locHigherBound = [locLowerBound[0] + locBinSizeOffset + 1]
    locFrequencyList = []

    while (DATA_LIST[-1] > locHigherBound[-1]):
        locLowerBound.append(locLowerBound[-1] + locBinSizeOffset)
        locHigherBound.append(locHigherBound[-1] + locBinSizeOffset)
    
    indexOfBounds = 0
    frequency = 0
    while len(DATA_LIST) != 0:
        if locLowerBound[indexOfBounds] <= DATA_LIST[0] <= locHigherBound[indexOfBounds]:
            frequency += 1
            DATA_LIST.pop(0)
        else:
            locFrequencyList.append(frequency)
            frequency = 0
            indexOfBounds += 1
    
    # display result
    for index in range(len(locFrequencyList)):
        print(str(locLowerBound[index]) + "-" + str(locHigherBound[index]), str(locFrequencyList[index]))


    # debugging
    print(DATA_LIST)
    print(locFrequencyList)
    # print(locLowerBound)
    print(locHigherBound)
    # end debugging 



if __name__ == "__main__":
    main()
