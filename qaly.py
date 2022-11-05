n=int(input())

qualy=0
for x in range(0, n):
    q,y=input().split()
    q=float(q)
    y=float(y)
    qualy = qualy + q*y
    
print(qualy)
    