n=int(input())

for i in range(0,n):
    m=int(input())
    
    d=dict()
    for j in range(0,m):
        s=input()
        d[s] = 1
    
    print(len(d))
