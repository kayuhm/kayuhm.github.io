#!/usr/bin/python3

from math import ceil

def main():
  t = int(input())
  if t <= 0:
    pass # temporary
  else:
    # variable declarations
    array = []
    h = 0
    for i in range(t):
      h = int(input())
      if h <= 0:
        return
      else:
        array.append(h)

    for element in array:
      pyramid(element)

def pyramid(dimension):
  width = dimension * 2 - 1
  total_width = width ** 2
  total_mid = ceil(total_width / 2)
  middles = [total_mid]

  for big_row in range(dimension):
    for row in range(dimension):
      for col in range(total_width):
        for element in middles:
          if element - 1 - row <= col <= element - 1 + row:
            print('*', end="")
          else:
            print(' ', end="")
      print(' ')

    if big_row != 0:
      middles.append(total_mid - big_row * width)
      middles.append(total_mid + big_row * width)

if __name__ == "__main__":
  main()
