from statistics import mean

n, x = (map(int, input().split()))
ar = []

for i in range(x):
    ar.append(list(map(float, input().split())))

s = zip(*ar)

for i in s:
    print (mean(i))
