from collections import *
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())
def nf(): return float(INP())

# Returns next line
def nl(): return [_ for _ in INP().split()]

V=['a', 'o', 'e', 'i', 'u']
ss=nl()[0]
a=0
b=0
for x in ss:
	if x in V:
		a += 1
		b += 1
	if x == 'y':
		b+=1
print(a, b)
