# this is my fine attempt to
# ascii art l0l

#  ****      *****
#    |        |
#     
#        A
# 
#     ________
import re
import sys
lines = sys.stdin.readlines()

counterzz = []

for i,line in enumerate(lines):
  if re.findall("FBI", line):
    counterzz.append(i)

if len(counterzz) == 0:
  print("HE GOT AWAY!")
else:
  print(" ".join([str(i+1) for i in counterzz]))
