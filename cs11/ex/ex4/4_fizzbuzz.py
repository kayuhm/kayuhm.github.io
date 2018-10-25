#!/usr/bin/python3

def main():
    t = int(input())
    if t > 0:
            a = 0
            b = 0
            c = 0
            a_array = []
            b_array = []
            c_array = []
            for counter in range(t):
                a = int(input())
                a_array.append(a)
                b = int(input())
                b_array.append(b)
                c = int(input())
                c_array.append(c)
        
            for a_element, b_element, c_element in zip(a_array, b_array, c_array):
                fizzbuzz(a_element, b_element, c_element)
def fizzbuzz(A, B, C):
    if (C == 0) or (C > 0 and A > B) or (C < 0 and A < B):
        print("Invalid Input!")
    else:
        text = ""
        if C > 0:
            B = B + 1
        else:
            B = B - 1
        for i in range(A, B, C):
            text = ""
            if (i % 3 == 0):
                text += "Fizz"
            if (i % 5 == 0):
                text += "Buzz"
            if (text == ""):
                text = str(i)
            print(text)
    print()


if __name__ == "__main__":
    main()
