from itertools import combinations_with_replacement
inp= input().split()
for c in list(combinations_with_replacement(sorted(inp[0]), int(inp[1]))):
    print (*c, sep='')
