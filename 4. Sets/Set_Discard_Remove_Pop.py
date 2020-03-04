n = int(input())
s = set(map(int, input().split()))
o = int(input())
for i in range(0,o):
    string= input().split()
    if (string[0]=="pop"):
        s.pop()
    elif (string[0]=="remove"):
        num= int(string[1])
        s.remove(num)
    else:
        num= int(string[1])
        s.discard(num) 

print (sum(s))
