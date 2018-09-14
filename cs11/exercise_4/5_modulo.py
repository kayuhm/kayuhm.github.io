#!/usr/bin/python3

def main():
    t = int(input())
    if t > 0:
        # variable declarations
        a_array = []
        n_array = []
        a = 0
        n = 0
        for i in range(t):
            a = int(input())
            if a < 0:
                return
            else:
                a_array.append(a)
            n = int(input())
            if n < 0:
                return
            else:
                n_array.append(n)

        for a_element, n_element in zip(a_array, n_array):
            modInverse(a_element, n_element)

def modInverse(A, N):
    multiplier = 1
    while multiplier <= N:
        multiplier = multiplier + 1
        if (A * multiplier) % N == 1:
            print(multiplier)
            break
        elif multiplier == N:
            print("DOES NOT EXIST")

if __name__ == "__main__":
    main()
