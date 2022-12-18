from collections import *
import sys
line = sys.stdin.read().split()

ok=True
d = set()
for w in line:
  if w in d:
    ok=False
    break

  d.add(w)

if ok:
  print("yes")
else:
  print("no")
