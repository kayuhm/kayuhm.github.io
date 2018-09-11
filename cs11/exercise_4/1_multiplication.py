#!/usr/bin/python3

def main():
  t = int(input())
  if t <= 0:
    pass # temporary
  else:
    # variable declarations
    array = []
    n = 0
    for i in range(t):
      n = int(input())
      if n <= 0:
        return
      else:
        array.append(n)
    
    for element in array:
      plot(element)

def plot(dimension):
  for i in range(1, dimension + 1):
    for k in range(1, dimension + 1):
      print(i * k, end='\t')
    print('\n')
  print('\n')


if __name__ == "__main__":
  main()
