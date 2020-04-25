from collections import Counter

X = int(input()) 
sizes = Counter(list(map(int, input().split())))
customers = int(input())
money = 0
for i in range(customers):
    a,b = list(map(int, input().split()))
    if (sizes[a] > 0):
        money += b
        sizes[a]-=1

print (money)
