from itertools import groupby
for k,c in groupby(input()):
    print ((len(list(c)), int(k)), end=' ')
