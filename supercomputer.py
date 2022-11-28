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

N,K=nl()
N=int(N)
K=int(K)
tree = Fenwick(N+1)

for x in range(0, K):
  l = nl()
  opcode=l[0]
  #print("Before: ", end="")
  #print(tree.data)
  if (opcode == "F"):
    a = int(l[1])
    if (tree.query(a, a) == 1):
      tree.dec(a, 1)
    else:
      tree.inc(a, 1)
  else:
    a = int(l[1])
    b = int(l[2])
    print(tree.query(a, b))

  #print("After:  ", end="")
  #print(tree.data)
