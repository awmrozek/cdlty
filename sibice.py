n,w,h=input().split()
n=int(n)
w=int(w)
h=int(h)

hyp = w*w + h*h
for x in range(0, n):
    t = int(input())
    if (t*t <= hyp):
        print("DA")
    else:
        print("NE")