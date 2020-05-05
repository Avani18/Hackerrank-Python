from collections import namedtuple
students = int(input())
columns = input().split()
mytup = namedtuple('mytup', columns)
marks = [int(mytup._make(input().split()).MARKS) for _ in range(students)]
print ((sum(marks))/(len(marks)))
