from fractions import Fraction
from bisect import bisect_left
n, c = map(int, input().split())
pos = []
for i in range(n):
    pos.append(int(input()))

lines = []
def intersect(k1, m1, k2, m2):
  # (m1 - m2) / (k2 - k1)
  return Fraction(m2-m1, k1-k2)

li = 0
def addLine(k, m):
  while True:
    previx, prevk, prevm = lines[-1]
    ix = intersect(prevk, prevm, k, m)
    if ix > previx:
      lines.append((ix, k, m))
      break
    else:
      lines.pop()
      global li
      li = min(li, len(lines)-1)

def queryLines(x):
  global li
  while li < len(lines) and x >= lines[li][0]:
    li += 1

  assert li != 0
  li -= 1
  _, k, m = lines[li]
  return k * x + m

dp = [0] * (n + 1)
lines.append((-1E9, pos[n-1], dp[n] + pos[n-1]**2))
for i in range(n-1, -1, -1):
  ans = queryLines(-2 * pos[i])
#  ans = 1E9
  #for j in range(i + 1, n + 1):
  #  ans = min(ans, dp [j] + -2*pos[i]*pos[j-1] + pos[j-1]**2)
  dp[i] = ans + c + pos[i]**2
  if i != 0:
    addLine(pos[i-1], dp[i] + pos[i-1]**2)
print(dp[0])

