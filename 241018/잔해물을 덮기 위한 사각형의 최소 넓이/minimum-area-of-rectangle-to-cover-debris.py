offset = 1000
total = 2001
checked = [[0]* total for _ in range(total)]
first = tuple(map(lambda x : x + offset, map(int, input().split())))
sec = tuple(map(lambda x : x + offset, map(int, input().split())))

for i in range(first[0], first[2]+1):
    for j in range(first[1], first[3]+1):
        checked[i][j] = 1

xS = max(first[0], sec[0])
xE = min(first[2], sec[2])
yS = max(first[1],sec[1])
yE = min(first[3],sec[3])

if xS < xE and yS < yE:        
    for i in range(xS,xE+1):
        for j in range(yS,yE+1):
            checked[i][j] = 0

sum = 0
for i in range(total):
    for j in range(total):
        if checked[i][j]:
            sum += 1
print(sum)