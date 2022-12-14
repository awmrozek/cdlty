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
d=[]

for i in range(2,n+1):
  di = ni()
  d = d + [[di, i]]

d=sorted(d)

print("1 ", end="")
for x in d:
  print(x[1], end=" ")
print("")
