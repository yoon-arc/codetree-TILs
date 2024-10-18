N = int(input())
total = 201
rects = [tuple(map(int, input().split())) for _ in range(N)] 
checked = [[0]*total for i in range(total)]

for x1,y1,x2,y2 in rects:
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100
    for i in range(x1, x2):
        for j in range(y1, y2):
            checked[i][j] = 1

sum = 0
for i in range(total):
    for j in range(total):
        if checked[i][j]:
            sum +=1
print(sum)
# print(checked)