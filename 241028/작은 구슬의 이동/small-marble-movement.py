n, t  = map(int, input().split()) #행 정보
r,c,d = input().split() #초기 행, 열, 방향
nx, ny = int(r), int(c)

mapper = {'U':0, 'R':1, 'L':2, 'D':3}
dxs, dys = [0,1,-1,0],[1,0,0,-1]
dx, dy = dxs[mapper[d]], dys[mapper[d]]


def in_range(x,y):
    return 1<= x <=n and 1<= y <=n
    
for _ in range(t+1):# 전체 반복
    # print("방향",dx,dy)
    nx += dy
    ny += dx

    if not in_range(nx,ny):
        dx *= -1
        dy *= -1


    
    
            


print(nx, ny)