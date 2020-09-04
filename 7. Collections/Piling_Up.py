t = int(input())
for _ in range(t):
    input()
    lst = list(map(int, input().split()))
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    if i == l - 1:
        print ("Yes")
    else:
        print ("No")
