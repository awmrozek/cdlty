s=input()
whitespaces=0
lowercase=0
uppercase=0
symbols=0
for t in s:
    if t == '_':
        whitespaces = whitespaces + 1
    elif t >= 'a' and t <= 'z':
        lowercase = lowercase + 1
    elif t >= 'A' and t <= 'Z':
        uppercase = uppercase + 1
    else:
        symbols = symbols + 1
        
print(whitespaces/len(s))
print(lowercase/len(s))
print(uppercase/len(s))
print(symbols/len(s))
