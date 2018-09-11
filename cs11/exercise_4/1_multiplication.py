#!/usr/bin/python3

n = int(input())
curr = 1

if (n <= 0):
  pass
else:
  for i in range (1,n+1):

    for j in range (curr, i+1):
        
      for k in range(1,i+1):
        print(curr * k, end='\t')

      print('\n')
      curr += 1
    
    curr = 1
    print('\n' * 2)
