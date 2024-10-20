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
            # if checked[i][j] == '1':
                checked[i][j] = 'y'


minX, minY = total, total
maxX, maxY = 0, 0

for i in range(total):
    for j in range(total):
        if checked[i][j] == '1':
            # 위치 업데이트!! 중요한 부분!
            minX = min(minX, i)
            maxX = max(maxX, i)
            minY = min(minY, j)
            maxY = max(maxY, j)

# 남은 직사각형의 길이와 높이 계산
if minX <= maxX and minY <= maxY:
    length = maxX - minX + 1
    height = maxY - minY + 1
    # print(length, height)
    print(length * height)
else:
    print(0)