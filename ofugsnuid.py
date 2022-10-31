n=int(input())

l=list()
for x in range(0,n):
    s = input()
    l = l + [s]
    
#for x in reversed(l):
for x in range(0,n):
    print(l[n-x-1])
