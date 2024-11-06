N, M = map(int, input().split())
#체크용
check = [[0]*M for _ in range(N)]
#범위 내 있는 지 체크
def in_range(h,y):
    return 0<=h<N and 0<=y<M
#방향키
dhs, dys = [1,0,-1,0],[0,1,0,-1]
#시작지점
h = y = d = 0
check[h][y] = 1

#N*M번 만큼 반복문 돌리기(i값 대입하기, 1, N*M+1)
for i in range(2, N*M+1):
    nh, ny = h+dhs[d],y+dys[d]
    if not in_range(nh,ny) or check[nh][ny] != 0:
        d = (d+1)%4
        
    h, y = h+dhs[d],y+dys[d]
    check[h][y] = i
    
        
    #범위 내 있지 않거나 값이 있을 때
        #현재 방향을 90도 전환
    #범위 내에 있으면서 값이 0 일때
        #현재 값에 i 대입

#check를 전부 출력
for i in check:
    print(*i, sep=" ")