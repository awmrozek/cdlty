from collections import *
import sys

points = 0
for line in sys.stdin:
  len2 = int(len(line)/2)
  right = line[len2:][:-1]
  left = line[:len2]

  s1 = set()
  for t in left:
    s1.add(t)

  s2 = set()
  for t in right:
    s2.add(t)

  p = (list(set.intersection(s1, s2))[0])

  if (ord(p) >= ord('A') and ord(p) <= ord('Z')):
    tp = int(ord(p)-ord('A')+27)
  else:
    tp = int(ord(p)-ord('a')+1)

  points = points + tp

print (points)

