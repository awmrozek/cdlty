from collections import *
import re
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())
def nf(): return float(INP())

# Returns next line
def nl(): return [_ for _ in INP().split()]

n=int(''.join(nl()))
m=int(''.join(nl()))

htot = 0
dtot = 0
for x in range(0, m):
	line = nl()
	l = ''.join(line)
	h = len(re.findall(r"#", l))
	d = len(l) - h
	htot += h
	dtot += d

print(dtot/(dtot+htot))
