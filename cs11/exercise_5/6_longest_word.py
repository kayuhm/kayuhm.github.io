def main():
    t = int(input())
    if t <= 0:
        pass
    else:
        arrInput = []
        for i in range(t):
            arrInput.append((input()).split())
        for element in arrInput:
            printLargest(element)

        

def printLargest(ARRAY_OF_WORDS):
    if len(ARRAY_OF_WORDS) == 1:
        print(ARRAY_OF_WORDS[0])
    else:
        largest = 0
        for index in range(1,len(ARRAY_OF_WORDS)):
            if len(ARRAY_OF_WORDS[index]) > len(ARRAY_OF_WORDS[largest]):
                largest = index
        print(ARRAY_OF_WORDS[largest])    

if __name__ == "__main__":
  main()
