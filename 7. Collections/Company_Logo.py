from collections import Counter

s = input()
c = dict(Counter(s))
sc = sorted(c.items(), key=lambda x: x[0], reverse=False)
ssc = sorted(sc, key=lambda x: x[1], reverse=True)
ch = 0
for i,j in ssc:
    print (i,j)
    ch += 1
    if ch == 3:
        exit()
