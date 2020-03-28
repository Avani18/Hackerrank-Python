from itertools import product
list1, list2= list(map(int, input().split())), list(map(int, input().split()))
for x in list(product(list1, list2)):
    print (x, end=" ")
