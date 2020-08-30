from collections import OrderedDict

n = int(input())
ordict = OrderedDict()
for _ in range(n):
    item, space, qty = input().rpartition(' ')
    ordict[item] = ordict.get(item, 0) + int(qty)

for item, qty in ordict.items():
    print (item, qty)
