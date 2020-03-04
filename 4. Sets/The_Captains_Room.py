k, listr= int(input()), list(map(int, input().split()))
myset= set(listr)
print (int(((sum(myset)*k)-sum(listr))/(k-1)))
