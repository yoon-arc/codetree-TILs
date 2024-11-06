N, M = map(int, input().split())
check = [[0]*M for _ in range(N)]

#범위 내 있는지 체크할 함수
def in_range(h,y):
    return 0<=h<N and 0<=y<M

#방향 전환 키
dhs, dys = [0,1,0,-1],[1,0,-1,0]

#현재 지점과 시작 방향
h = y = d = 0

#시작 지점에 A를 지정하고
# check[h][y] = 'A'

#ord용 변수
alp = 65

#2, N*M+1만큼 반복
for i in range(N*M):
    #다시 A부터 반복할 수 있게
    nh, ny = h+dhs[d],y+dys[d]
    if not in_range(nh,ny) or check[nh][ny] != 0:
        d = (d+1)%4
    check[h][y] = chr(alp)
    h, y = h+dhs[d],y+dys[d]
    alp += 1
    if alp > 90:
        alp = 65


for i in check:
    print(*i, sep=" ")
# print(check)