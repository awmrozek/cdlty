import sys

wordphrase = sys.stdin.readline()

eh = wordphrase[::-1]

if (len(eh) >= 4 and eh[1] == '?' and eh[2] == 'h' and eh[3] == 'e'):
  print("Canadian!")
else:
  print("Imposter!")
