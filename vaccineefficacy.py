from collections import *
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())
def nf(): return float(INP())

# Returns next line
def nl(): return [_ for _ in INP().split()]

N=int(ni())

pap = 0
pan = 0
pbp = 0
pbn = 0
pcp = 0
pcn = 0

nap = 0
nan = 0
nbp = 0
nbn = 0
ncp = 0
ncn = 0

for i in range(0, N):
  s = nl()[0]
  
  z = s[0]
  a = s[1]
  b = s[2]
  c = s[3]

  if z == 'N':
    if a == 'N':
      nan = nan + 1
    else:
      nap = nap + 1

    if b == 'N':
      nbn = nbn + 1
    else:
      nbp = nbp + 1

    if c == 'N':
      ncn = ncn + 1
    else:
      ncp = ncp + 1
  # ##############################
  else:
    if a == 'N':
      pan = pan + 1
    else:
      pap = pap + 1

    if b == 'N':
      pbn = pbn + 1
    else:
      pbp = pbp + 1

    if c == 'N':
      pcn = pcn + 1
    else:
      pcp = pcp + 1

hpa = (nap/(nap+nan))
lpa = (pap/(pap+pan))
ansa = (hpa-lpa)/hpa

hpb = (nbp/(nbp+nbn))
lpb = (pbp/(pbp+pbn))
ansb = (hpb-lpb)/hpb

hpc = (ncp/(ncp+ncn))
lpc = (pcp/(pcp+pcn))
ansc = (hpc-lpc)/hpc

NE="Not Effective"
if (ansa <= 0):
  print(NE)
else:
  print(ansa*100)

if (ansb <= 0):
  print(NE)
else:
  print(ansb*100)

if (ansc <= 0):
  print(NE)
else:
  print(ansc*100)
