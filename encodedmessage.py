#!/usr/bin/python
import math
n=int(input())

def myReshape(a, b):
  res = []
  for i in range(0, b):
    line = [a[j] for j in range(i*b, (i*b)+b)]
    res = res + [line]
  return res

def myTranspose(a, l):
  calyciag = []
  # indices of elements of a in right order
  ciag = [x*l for x in range(1, l+1)]
#  print(ciag)

  while (ciag[0] > 0):
    calyciag = calyciag + ciag
    ciag = [x-1 for x in ciag]

  return ''.join(a[i-1][0] for i in calyciag)


for i in range(0, n):
  s=input().split()[0]
  a=[[x] for x in s]
  b=int(math.sqrt(len(s)))
  
  decoded = myTranspose(a, b)
  print(decoded)

#  rres = []
#  for msg in decoded:
#    res = ""
#    for i in range(0, len(msg)):
#      res = res + ''.join(msg[i])
#    rres = rres + [res]
#  for i in range(0, b):
#    print(rres[len(rres)-i-1], end="")
#  print("")
