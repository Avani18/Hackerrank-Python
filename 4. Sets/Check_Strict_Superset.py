A= set(input().split())
n= int(input())
for i in range(n):
    check= set(input().split())
    if ((check.issubset(A)) and (len(A)>len(check))):
        continue
    else: 
        print ("False")
        exit()
if (i==n-1):
    print("True")
