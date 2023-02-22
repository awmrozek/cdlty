from collections import *
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())
def nf(): return float(INP())

# Returns next line
def nl(): return [_ for _ in INP().split()]

n=int(ni())
p=int(ni())
s=int(ni())

for i in range(0, s):
  m = int(ni())
  l = list()
  for j in range(0, m):
    t = int(ni())
    l = l + [t]
  if p in l:
    print("KEEP")
  else:
    print("REMOVE")
