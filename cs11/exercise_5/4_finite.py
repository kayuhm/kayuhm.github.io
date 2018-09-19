#!/usr/bin/env env python3

def main():
    t = int(input())
    if t <= 0:
        # saved for invalid input output
        pass
    else:
        array_of_list = []
        for i in range(t):
            array_of_list.append(input().split())
        for each_list in array_of_list:
            for index in range(len(each_list)):
                each_list[index] = int(each_list[index])
        for each_list in array_of_list:
            finite(each_list)

def finite(ARRAY):
    if (len(ARRAY) == 1):
        print(str(ARRAY[0]))
    else:
        local_prev = ARRAY.pop(0)
        print(str(round(local_prev + recursive(ARRAY), 6))) # RECURSION

def recursive(ARRAY):
    if len(ARRAY) == 2:
        return (1 /(ARRAY[0] + ARRAY[1]))
    else:
        local_prev = ARRAY.pop(0)
        return (1 / (local_prev + recursive(ARRAY)))

if __name__ == "__main__":
    main()
