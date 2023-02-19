n=int(input())

for j in range(0,n):
    a=input()
    b=input()
    
    rstr=""
    print(a)
    print(b)
    for i in range(0,len(a)):
        if (a[i] == b[i]):
            print(".",end="")
        else:
            print("*",end="")
    print("")
    print("")
