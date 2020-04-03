from itertools import combinations
n= int(input())
total_combinations= tuple(combinations(list(input().split()), int(input())))
counter= 0
for i in total_combinations:
    if ('a' in i):
        counter+=1
print (counter/len(list(total_combinations)))
