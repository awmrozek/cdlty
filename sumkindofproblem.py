n=int(input())

for i in range(0, n):
  a,n=input().split()

  a=int(a)
  n=int(n)

  # s1 - first N positive integers
  # s2 - first odd integers
  # s3 - first n even integers
  s1 = int(n*(n+1)/2)
  s2 = n*n
  s3 = n*(n+1)

  print(a, s1, s2, s3)
