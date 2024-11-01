N, M = map(int, input().split())
check = [[0]*N for _ in range(N)]
dys,dhs = [1,0,-1,0],[0,1,0,-1]

def in_range(x,y):
    return 0<= x and x < N and  0<= y and y < N

for _ in range(M):
    h, y = map(int, input().split())
    h -= 1
    y -= 1
    # print(h,y)
    # print(f"새로운 {h,y}")

    count = 0

    for cy, ch in zip(dys,dhs):
        ny, nh = y+cy, h+ch
        # print(nh,ny)
        if in_range(nh,ny) and check[nh][ny] == 1:
            # print(nh,ny)
            count += 1
    if count == 3:
        print(1)
    else:
        print(0)
    check[h][y] = 1