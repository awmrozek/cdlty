from collections import *
from math import pi
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())
def nf(): return float(INP())

# Returns next line
def nl(): return [_ for _ in INP().split()]

N=int(ni())
for i in range(0,N):
  r=int(ni())
  n=int(ni())

  nocircles = 0
  area = 0
  for i in range(0,n):
    if i == 0:
      area = 1 * pi*r*r
      nocircles = 1
    elif i == 1:
      area = area + 4 * pi*r*r
      nocircles = 4
    else:
      area = area + nocircles * 3 * pi*r*r
      nocircles = nocircles *3 
#    print(r, area)
    r = r / 2

  print(area)
