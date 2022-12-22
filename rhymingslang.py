from collections import *
import sys
#itr = [line for line in sys.stdin.read().split()]

S = sys.stdin.readline()[:-1]
E = int(sys.stdin.readline())

mlist=set()
for i in range(0,E):
  l=sys.stdin.readline().split()

  append=False
  llist=[]
  for t in l:
    nbytes=len(t)
    a=S[-nbytes:]
    b=t

    if (a == b):
      append = True
      #print("The line {} rhymes".format(l))
    #print(S[-nbytes:], t)
  if append:
    for t in l:
      mlist.add(t)

P = int(sys.stdin.readline())
for i in range(0, P):
  t = sys.stdin.readline().split()[-1:][0]

  match = False
  for x in mlist:
    nbytes=len(x)
    a=x[-nbytes:]
    b=t[-nbytes:]
    #print(a, b)

    if (a == b):
      match = True

  if match:
    print("YES")
  else:
    print("NO")


