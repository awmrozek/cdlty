n=int(input())

if (n % 2 ==0):
    sum=0
    for x in range(0, int(n/2)):
        a=int(input())
        b=int(input())
        sum=sum+(b-a)
    print(sum)
else:
    print("still running")
