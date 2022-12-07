from collections import *
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())

# Returns next line
def nl(): return [int(_) for _ in INP().split()]

n=ni()
c=[ni() for _ in range(0, n)]
c=sorted(c)
b=[i for i in range(1, n+1)]

f = 999
for i in range(0, n):
  if c[i] <= b[i]:
    f = min(f, c[i]/b[i])
  else:
    f = 999
    break

if f == 999:
  print("impossible")
else:
  print(f)
