from collections import *
import sys
itr = (line for line in sys.stdin.read().split("\n"))
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return int(INP())
def nf(): return float(INP())

N=int(INP())
words = []
for i in range(0, N):
	words.append(INP())

words = ' '.join(words).lower()
sentence = INP().split()

for word in sentence:
	if word.lower() not in words:
		print("Thore has left the chat")
		exit(0)

print("Hi, how do I look today?")

