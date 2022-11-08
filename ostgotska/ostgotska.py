#!/usr/bin/python
s=input().split()

a=sum([t.find("ae") >= 0 for t in s])
b=len(s)

if a/b > 0.4:
  print("dae ae ju traeligt va")
else:
  print("haer talar vi rikssvenska")
