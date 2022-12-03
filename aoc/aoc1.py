from collections import *
import sys

maxglob = 0
maxloc = 0

l=list()
for line in sys.stdin.readlines():
  line = line[:-1]
  if line == "":
    l.append(maxloc)
    maxloc = 0
  else:
    i=int(line)
    maxloc = maxloc + i

l.append(maxloc)
l=sorted(l)
threelast = (l[-3:])
print(threelast)
print (sum(threelast))

