from collections import *
import sys
itr = (line for line in sys.stdin.read().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

N=ni()
a=set(nl())
b=set(nl())
print (list(a.difference(b))[0])

