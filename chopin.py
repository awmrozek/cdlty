from collections import *
import sys

i = 0
for line in sys.stdin:
    i += 1
    line = line[:-1]
    res = ""
    d = {
      "A# minor": "Bb minor", #
      "A# major": "Bb major",
      "C# major": "Db major",
      "Db minor": "C# minor",
      "D# minor": "Eb minor",
      "D# major": "Eb major",
      "Gb minor": "F# minor",
      "Gb major": "F# major",
      "Ab minor": "G# minor",
      "G# major": "Ab major",

      "Bb minor": "A# minor", #
      "Bb major": "A# major",
      "Db major": "C# major",
      "C# minor": "Db minor",
      "Eb minor": "D# minor",
      "Eb major": "D# major",
      "F# minor": "Gb minor",
      "F# major": "Gb major",
      "G# minor": "Ab minor",
      "Ab major": "G# major"

    }

    if line in d:
      print(f"Case {i}: {d[line]}")
    else:
      print(f"Case {i}: UNIQUE")

