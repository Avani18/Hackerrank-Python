for i in range(int(input())):
   m, A, n, B= int(input()), set(input().split()), int(input()), set(input().split())
   print (A.issubset(B))
