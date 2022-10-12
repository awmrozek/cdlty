n=int(input())

ssum=0
for i in range(0,n):
    x=input()
    ba=int(x[:-1])
    ex=int(x[-1:])
    ssum = ssum + ba**ex

print(ssum)
