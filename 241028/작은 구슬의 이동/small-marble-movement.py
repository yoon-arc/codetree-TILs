n, t  = map(int, input().split()) #행 정보
r,c,d = input().split() #초기 행, 열, 방향
nh, ny = int(r), int(c)

mapper = {'U':0, 'R':1, 'L':2, 'D':3}
reoul, hang = [0,1,-1,0],[-1,0,0,1]
dy, dh = reoul[mapper[d]], hang[mapper[d]]


def in_range(x,y):
    return 1<= x <=n and 1<= y <=n
    
for _ in range(t):# 전체 반복
    # print("방향",dh,dy)
    nh += dh
    ny += dy

    if not in_range(nh,ny):
        dh *= -1
        dy *= -1
        nh += dh
        ny += dy

print(nh, ny)