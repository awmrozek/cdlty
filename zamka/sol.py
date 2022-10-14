l=int(input())
d=int(input())
x=int(input())

# L < N < D
# L < M < D

def sumdig(n):
    return sum([int(t) for t in str(n)])
    
minn = l
for n in range(l, d+1):
    if (sumdig(n) == x):
        minn = n
        break
    
maxm = d
for m in reversed(range(l, d+1)):
    if (sumdig(m) == x):
        maxm = m
        break
    
print(minn)
print(maxm)
