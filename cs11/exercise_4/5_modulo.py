#!/usr/bin/python3

def main():
    t = int(input())
    if t <= 0:
        pass # temporary
    else:
        # variable declarations
        a_array = []
        n_array = []
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

        for a_element, n_element in a_array, n_array:
            modInverse(a_element, n_element)

def modInverse(A, N):
    print(str(A) + " " + str(N))

if __name__ == "__main__":
    main()
