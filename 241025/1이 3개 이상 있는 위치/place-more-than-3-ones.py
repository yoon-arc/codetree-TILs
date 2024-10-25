n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs,dys = [1,0,-1,0],[0,-1,0,1]

def in_range(x,y) :
    return 0<= x and x<n and 0<= y and y < 4
count = 0

for i in range(len(grid)):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs,dys):
            nx, ny = i+dx, j+dy
            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            count+=1

print(count)