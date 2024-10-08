m1, d1, m2, d2 = map(int, input().split())
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
if m1 == m2:
    getDay = (months[m1] - d1+1)%7
else:
    getDay = ((months[m1] - d1) + sum(months[m1:m2]) + d2)%7
print(days[getDay])