n=int(input())

for j in range(0,n):
    a=input()
    b=input()
    
    rstr=""
    for i in range(0,len(a)):
        if (a[i] == b[i]):
            print("*",end="")
        else:
            print(".",end="")
    print("")