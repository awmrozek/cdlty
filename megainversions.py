# This is too slow to pass on kattis
# but I believe it gives the right results anyway
from collections import *
import sys
itr = (line for line in sys.stdin.read().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
# Next line
def nl(): return [_ for _ in INP().split()]

class Fenwick:
  def __init__(self, N):
    self.data = [0]*(N+1)

  def sum(self, i):
    acc = 0
    i += 1
    while i > 0:
      acc += self.data[i]
      i -= i&(-i)
    return acc

  def inc(self, i, delta):
    i += 1
    while i < len(self.data):
      self.data[i] += delta
      i += i&(-i)

  def dec(self, i, delta):
    i += 1
    while i < len(self.data):
      self.data[i] -= delta
      i += i&(-i)

  def query(self, l, r):
    # inclusive l, r
    # l - 1 i want L as well
    right = self.sum(r)
    left  = self.sum(l - 1)
    #print("Right: {}", right)
    #print("Left:  {}", left)
    return right - left

class BinaryNode:
  def __init__(self, v, ix):
    self.l = None
    self.r = None
    self.v = v
    self.ix = ix

  def add(self, v, ix):
    #    print(f"add {v} index {ix}")
    if v < self.v:
      if self.l is None:
        self.l = BinaryNode(v, ix)
      else:
        self.l.add(v, ix)
    else:
      if self.r is None:
        self.r = BinaryNode(v, ix)
      else:
        self.r.add(v, ix)

  def retreive(self, v):
    #    print(f"retreive {v} from {self.v}")
    if self.v <= v:
      return ([] if (self.r is None) else self.r.retreive(v))
    else:
      el = ([] if (self.l is None) else self.l.retreive(v)) \
          + ([] if (self.r is None) else self.r.retreive(v)) + [self.ix]
#      print(f"\"tom\" lista {el}")
      return el

N = ni()
inputs = [int(x) for x in nl()]
ixi = 0

f = Fenwick(N+2)
left_side = [0 for _ in range(0, N)]
right_side = [0 for _ in range(0, N)]

tree = BinaryNode(inputs[ixi], 0)
ixi += 1
for i in range(1, N):
  el = inputs[ixi]
  ixi += 1
  matches = tree.retreive(el)
  right_side[i] += len(matches)
  for m in matches:
    left_side[m] += 1
  tree.add(el, i)

s = 0
for i in range(0, N):
  s += left_side[i] * right_side[i]
  #print(f"{left_side[i]} {right_side[i]}")

print(s)
