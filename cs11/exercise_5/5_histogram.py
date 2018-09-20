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
    DATA_LIST.sort()
    locBinSizeOffset = int(BIN_SIZE) - 1
    locLowerBound = [int(DATA_LIST[0])]
    locHigherBound = [locLowerBound[0] + locBinSizeOffset]
    locFrequency = []

    while (int(DATA_LIST[-1]) > locHigherBound[-1]):
        locLowerBound.append(locLowerBound[-1] + locBinSizeOffset)
        locHigherBound.append(locHigherBound[-1] + locBinSizeOffset)

    frequency = 0
    indexOfBounds = 0
    for index in range(len(DATA_LIST) - 1):
        if locLowerBound[indexOfBounds] < int(DATA_LIST[index]) < locHigherBound[indexOfBounds]:
            frequency += 1
        else:
            locFrequency.append(frequency)
            frequency = 0
            indexOfBounds += 1


    # debugging
    print(DATA_LIST)
    print(locLowerBound)
    print(locHigherBound)
    # end debugging 

    



if __name__ == "__main__":
    main()
