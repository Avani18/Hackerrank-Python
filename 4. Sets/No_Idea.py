random= input()
mylist= list(map(int, input().split()))
happiness=0
A, B= set(map(int, input().split())), set(map(int, input().split()))
for i in mylist:
    if (i in A):
        happiness+=1
    elif (i in B):
        happiness-=1
print (happiness)
