from collections import *
import sys
itr = (line for line in sys.stdin.read().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

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

  def query(self, l, r):
    # inclusive l, r
    # l - 1 i want L as well
    return self.sum(r) - self.sum(l - 1)


def main():
  N = ni()
  P = [ni() for _ in range(N)]
  P2 = list(enumerate(P))
  P2.sort(key=lambda x: x[1])
  tree = Fenwick(N)
  acc = 0
  for idx, v in P2:
    acc += tree.query(idx, N-1)
    tree.inc(idx, 1)
  print(acc)
  

main()
