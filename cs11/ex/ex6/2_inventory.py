#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    t = int(input())
    l = []
    while t != 0:
        l = input().split()
        limit = int(l[1])
        final = []
        count = 1
        word = l[0]

        curr = word[0] # curr initialization
        while limit != 0:
            for index in range(len(word)):
                if word[index] == curr:
                    if index == len(word) - 1:
                        # if end of word
                        count += 1
                        final.append(str    count) + curr)
                    else:
                        count += 1
                else:
                    if index == len(word) - 1:
                        # if end of word
                        final.append(str    count) + curr)
                        final.append("1" + word[index])
                    else:
                        final.append(str    count) + curr)
                        count = 1
                        curr = word[index]
            t = 0
            word = ''.join(final)
            # print("final", final)
            # print("word", word)
            final = []
            curr = word[0]
            limit -= 1
        print(word) # this is it
        t -= 1

if __name__ == "__main__":
    main()
