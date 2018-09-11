#!/usr/bin/python3

def main():
  t = int(input())
  if t <= 0:
    pass # temporary
  else:
    # variable declarations
    array = []
    s = 0
    for i in range(t):
      s = int(input())
      if s <= 0:
        return
      else:
        array.append(s)
    
    for element in array:
      diamond(element)
      print('\n')

def diamond(side):
  mid = side
  length = side * 2 - 1

  # print the top part
  for i in range(mid):
    for j in range(length):
      if (mid - 1 - i <= j <= mid - 1 + i):
        print('*', end='')
      else:
        print(' ', end='')
    print('\n')

  # print the bottom part
  for i in range(mid - 2, -1, -1):
    for j in range(length):
      if (mid - 1 - i <= j <= mid - 1 + i):
        print('*', end='')
      else:
        print(' ', end='')
    print('\n')


if __name__ == "__main__":
  main()
