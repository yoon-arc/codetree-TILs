n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs,dys = [1,0,-1,0],[0,-1,0,1]
nx = ny = 0
count = 0

def in_range(x,y) :
    return 0<= x and x<n and 0<= y and y < n



for i in range(n): #행
    for j in range(n): #열
        #현재 좌표, 모든 방향 검사:
        cnt = 0
        for dx, dy in zip(dxs,dys):
            nx, ny = i+dx, j+dy
            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
                
        if cnt >= 3 :
            count += 1
            
print(count)