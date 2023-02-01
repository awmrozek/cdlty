from collections import *
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())
def nf(): return float(INP())

# Returns next line
def nl(): return [_ for _ in INP().split()]

x=int(ni())
y=int(ni())

v=[False for i in range(0,x+1)]
for i in range(0,y):
  t=int(ni())
  v[t] = True

list1 = []
def unterval(schminterval=False):
  global list1

  startInterval = -1
  stopInterval = -1
  countingInterval = False
  needComa = False
  
  for i in range(1,x+1):
    if v[i] == (not schminterval) and countingInterval == False:
      countingInterval = True
      startInterval = i
    if v[i] == schminterval and countingInterval == True:
      countingInterval = False
      stopInterval = i-1
      list1 = list1 + [(startInterval, stopInterval)]
  
  #print(countingInterval)
  if countingInterval:
    list1 = list1 + [(startInterval, x)]

def prettyString(tup):
  if tup[0] == tup[1]:
    return str(tup[0])
  else:
    return str(tup[0]) + "-" + str(tup[1])

def prettyList():
  print(prettyString(list1[0]), end="")
  if len(list1) > 1:
    for i in range(1, len(list1)-1):
      print(", {}".format(prettyString(list1[i])), end="")
    print(" and {}".format(prettyString(list1[len(list1)-1])))


unterval(False)
print("Errors: ", end="")
prettyList()

list1=[]
unterval(True)
print("Correct: ", end="")
prettyList()

