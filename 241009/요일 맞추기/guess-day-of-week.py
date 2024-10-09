m1, d1, m2, d2 = map(int, input().split())
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']

if  m1 > m2:
    getDay = ((months[m2] - d2) + sum(months[m2+1:m1]) + d1)
elif m1 == m2 and d2>= d1:
    getDay = d2 - d1
elif m1 == m2 and d1> d2:
    getDay = 7-(d1 - d2)
else:
    getDay = ((months[m1] - d1) + sum(months[m1+1:m2]) + d2)
    print(f"{sum(months[m1+1:m2])}")
    
getDay %= 7

print(days[getDay])