from math import ceil

def main():
    t = int(input())
    if t <= 0:
        pass
    else:
        arrInput = []
        for i in range(t):
            arrInput.append(int(input()))
        for element in arrInput:
            canonicalPrime(element)

        

def canonicalPrime(N):
    factor = 2
    limit = ceil(N / 2)
    arr_factors = []
    while (True):
        if N % factor == 0:
            arr_factors.append(factor)
            N = N / factor
            factor = 2
        if factor > limit:
            if N != 1:
                arr_factors.append(int(N))
            break
        factor += 1
    arr_factors.sort()element
    print(arr_factors)


if __name__ == "__main__":
  main()
