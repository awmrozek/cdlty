from collections import *
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())
def nf(): return float(INP())

# Returns next line
def nl(): return [_ for _ in INP().split()]

monnei=int(ni())
fjee=int(ni())
dolladollabilljoll=int(ni())

a = min(monnei, min(fjee, dolladollabilljoll))

if a == monnei:
	print("Monnei")
elif a == fjee:
	print("Fjee")
else:
	print("Dolladollabilljoll")
