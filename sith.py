import sys
jedi = sys.stdin.readline()
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

jedi = a - b
sith = [a - b if a > b else b - a]

if a > b:
  print("VEIT EKKI")
elif jedi == c:
  print("JEDI")
else:
  print("SITH")

# print(jedi, a, b, c)
