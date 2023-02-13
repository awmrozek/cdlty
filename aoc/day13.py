from collections import *
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())
def nf(): return float(INP())

# Returns next line
def nl(): return [_ for _ in INP().split()]

x=int(ni())
y=int(ni())

print(x)
print(y)

7,13,x,x,59,x,31,19

#x % 7 = 0
#x % 13 = 1
#x % 59 = 4
#x % 31 = 6
#x % 19 = 7

# Chinese reminder theorem
