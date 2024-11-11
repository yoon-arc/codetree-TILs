N, T = map(int, input().split())
grid = []
commands = list(input())
for _ in range(N):
    grid.append(list(map(int, input().split())))
dhs,dys = [-1,0,1,0],[0,1,0,-1]
s = (N-1)//2
h,y = s,s
d = 0
def in_range(h,y):
    return 0<=h<N and 0<=y<N
def get_direction(c):
    return (d-1+4)%4 if c == 'L' else (d+1)%4
result = 0
for c in commands:    
    if c != 'F' :
        d = get_direction(c)
    nh, ny = h+dhs[d],y+dys[d]
    if not in_range(nh,ny):
        continue
    result += grid[h][y]
    h, y = nh,ny
print(result)