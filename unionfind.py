from collections import *
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())
def nf(): return float(INP())

# Returns next line
def nl(): return [_ for _ in INP().split()]

class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.sz = [1]*N
    def find(self, i):
        path = []
        while i != self.parent[i]:
            path.append(i)
            i = self.parent[i]
        # path compression
        for u in path: self.parent[u] = i
        return i
    def union(self, u, v):
        uR, vR = map(self.find, (u, v))
        if uR == vR: return False
        if self.sz[uR] < self.sz[vR]:
            self.parent[uR] = vR
            self.sz[vR] += self.sz[uR]
        else:
            self.parent[vR] = uR
            self.sz[uR] += self.sz[vR]
        return True

N=int(ni())
Q=int(ni())

fu=UnionFind(N)

for i in range (0,Q):
  op = INP()
  a = ni()
  b = ni()

  if (op == "="):
    fu.union(a, b)
  else:
    print(["yes" if fu.find (a) == fu.find(b) else "no"][0])

