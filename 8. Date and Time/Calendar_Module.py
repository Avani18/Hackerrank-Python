from calendar import weekday
m, d, y = map(int, input().split())
days = {0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}
print (days[weekday(y, m, d)])
