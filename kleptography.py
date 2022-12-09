# Solution for problem kleptography from kattis
# This is an example of the critical point of something similar to 
# Ballmer's curve: tirednes increases linearly and difficulty of the problems
# increase exponentially. The critical point is the point where the two 
# curves meet.

# awmrozek 2022

from collections import *
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())

# Returns next line
def nl(): return [_ for _ in INP().split()]

n=ni()
m=ni()

p=nl()
c=nl()

res=[]
b = [ord(t) - ord('a') for t in c[0]];
a = [0 for x in range(0, len(b)-len(p[0]))] + [ord(t) - ord('a') for t in p[0]]

#  program logic --------------------------------------------------

#print(a) # key
#print(b) # encrypted

def decrypt(i):
  global a
  global b
  if (i < 0 or i > (len(b)-len(p[0])-1)):
    #print("Value out of range")
    pass
  else:
    #print("value decryptable")
    t1 = a[i+len(p[0])]
    t2 = b[i+len(p[0])]
    #print(t1, t2)
    t = (26 + t2 - t1) % 26
    #print(t)
    a[i] = t

for x in range(0, len(b)+1):
  decrypt(len(b)-x)

# result to ascii ------------------------------------------------
d = [chr(t + ord('a')) for t in a]
print(''.join(d))

