x=int(input())

for i in range(0,x):
    s=input().strip().split(' ')
    probid=int(s[0])
    days = int(s[1])
    
    cnadles = 0
    # Iterate through days
    for j in range(1, days+1):
        # Shammas
        cnadles = cnadles + j + 1

    print(str(probid) + " " + str(cnadles))
