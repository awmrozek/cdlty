#!/usr/bin/python
# DRM - Divide Rotate Merge
# Ugly solution for the simple problem
# There should probably be more list comprehensions

s=input()
# First half of string
a=s[:int(len(s)/2)]
a=list(a)
ai=[int(ord(t) - ord('A')) for t in a]

# Second half of string
b=s[int(len(s)/2):]
b=list(b)
bi=[int(ord(t) - ord('A')) for t in b]

rota = 0
rotb = 0

# Calculate rotation values
for c in ai:
  rota = rota + c

for c in bi:
  rotb = rotb + c

def rotstr(s, rotx):
  #print("Rotate string a by " + str(rotx) + " forward")
  # Rotate each string
  c=0
  for i in range(0, len(s)):
    c = ((s[i] + rotx) % 26);
    s[i] = c
  return s

ai=rotstr(ai, rota)
bi=rotstr(bi, rotb)
ci=list()

for i in range(0, len(ai)):
  ci.append((ai[i] + bi[i]) % 26)

print(''.join([chr(t + ord('A')) for t in ci]))

