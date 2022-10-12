s = input()
m = dict()
for x in s:
    if x in m:
        print("0")
        exit()
    m[x] = x
print("1")
