m=int(input())
seta= set(map(int,input().split()))
n=int(input())
setb= set(map(int,input().split()))

myset= seta.union(setb)
myseti= seta.intersection(setb)
mysetsd= myset.difference(myseti)
mylist=list(mysetsd)
mylist.sort()
for i in range(len(mylist)):
    print(mylist[i])
