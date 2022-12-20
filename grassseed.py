c=float(input())
l=int(input())

area=0
for i in range(0,l):
    wi, li = input().split()
    wi=float(wi)
    li=float(li)

    area = area + wi*li

print(area*c)`
