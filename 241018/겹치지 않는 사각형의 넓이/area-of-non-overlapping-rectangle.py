total = 2001
rects = [tuple(map(int, input().split())) for _ in range(3)]
checked = [[0]*total for _ in range(total)]

for x1,y1,x2,y2 in rects:
    x1 += 1000
    y1 += 1000
    x2 += 1000
    y2 += 1000
    if x1 == rects[2][0]+1000 and y1 == rects[2][1]+1000 and x2 == rects[2][2]+1000 and y2== rects[2][3]+1000:
        for i in range(x1,x2):
            for j in range(y1, y2):
                checked[i][j] = 0
    else:
        for i in range(x1,x2):
            for j in range(y1, y2):
                checked[i][j] = 1

sum = 0   
for i in range(total):
    for j in range(total):
        if checked[i][j]:
            sum += 1

print(sum)