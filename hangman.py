from collections import *
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())
def nf(): return float(INP())

# Returns next line
def nl(): return [_ for _ in INP().split()]

a=set(nl()[0])
b=nl()[0]
#print(b)
d=set()

i = 0
for c in b:
  if i >= 10:
    break
  if c in a:
    d.add(c)
  else:
    i = i + 1

#print(d)
#print(a)

if a==d:
  print("WIN")
else:
  print("LOSE")

