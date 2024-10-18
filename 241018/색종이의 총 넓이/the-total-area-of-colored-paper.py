offset = 100
total = 201
check = [[0]* 201 for _ in range(total)]
N = int(input())
rects = [tuple(map(int, input().split())) for _ in range(N)]
# print(rects)
for x,y in rects:
    x += 100
    y += 100
    for i in range(x,x+8):
        for j in range(y, y+8):
            check[i][j] = 1
            
sum = 0
for i in range(total):
    for j in range(total):
        if check[i][j]:
            sum += 1
            
print(sum)