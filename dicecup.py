from collections import *
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())
def nf(): return float(INP())

a = ni()
b = ni()

if a > b:
	c = b
	b = a
	a = c

for x in range(a+1, b+2):
	print(x)
