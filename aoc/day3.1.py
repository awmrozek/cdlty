from collections import *
import sys

points = 0

def mkset(line):
  len2 = int(len(line)/2)
  right = line[len2:][:-1]
  left = line[:len2]

  s1 = set()
  for t in line:
    s1.add(t)
  return s1


lines = [line for line in sys.stdin.readlines()]
print(lines)

while (len(lines) > 0):
  l1 = lines[0][:-1]
  l2 = lines[1][:-1]
  l3 = lines[2][:-1]
  print(l1, l2, l3)

  lines = lines[3:]

  s1 = mkset(l1)
  s2 = mkset(l2)
  s3 = mkset(l3)
  print(s1, s2, s3)

  ss = set.intersection(s1, set.intersection(s2, s3))
  p = (list(ss)[0])
  #p = (list(set.intersection(s1, s2))[0])
  print("intersection: ")
  print(ss)

  if (ord(p) >= ord('A') and ord(p) <= ord('Z')):
    tp = int(ord(p)-ord('A')+27)
  else:
    tp = int(ord(p)-ord('a')+1)

  print("local: {}".format(tp))
  points = points + tp

print(points)

