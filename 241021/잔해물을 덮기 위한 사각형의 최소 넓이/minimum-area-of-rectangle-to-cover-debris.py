offset = 1000
total = 2000
checked = [[0]* total for _ in range(total)]
first = tuple(map(lambda x : x + offset, map(int, input().split())))
sec = tuple(map(lambda x : x + offset, map(int, input().split())))

for i in range(first[0], first[2]):
    for j in range(first[1], first[3]):
        checked[i][j] = '1'

for i in range(sec[0], sec[2]):
    for j in range(sec[1], sec[3]):
        if (first[0] <= i < first[2]) and (first[1] <= j < first[3]):
            checked[i][j] = 'y'

length = 0
height = 0

for i in range(total):
    long = checked[i].count('1')
    if length < long:
        length = long
    if '1' in checked[i]:
        height += 1
print(length*height)