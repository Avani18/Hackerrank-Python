length= int(input())
myset= set(map(int, input().split()))
ops= int(input())
for i in range(ops):
    eval('myset.{0}({1})'.format(input().split()[0], set(map(int, input().split()))))
print (sum(myset))
