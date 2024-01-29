from collections import *
import sys
import re
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())
def nf(): return float(INP())

# Returns next line
def nl(): return [_ for _ in INP().split()]

covid = ''.join(nl())
# So much overkill mwa ha ha ha ha ha!!
if re.search("COV", covid):
	print("Veikur!")
else:
	print("Ekki veikur!")
