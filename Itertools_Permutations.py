from itertools import permutations
string, length= input().split()
for x in tuple(permutations(sorted(string), int(length))):
    print (*x, sep='')
