from collections import *
import sys
import re
s=input()
smiley=len(re.findall(r":\)", s))
frowny=len(re.findall(r":\(", s))

if smiley > 0 and frowny > 0:
    print("double agent")
elif smiley > 0:
    print("alive")
elif frowny > 0:
    print("undead")
else:
    print("machine")
