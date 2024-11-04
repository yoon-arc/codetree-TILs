N = int(input())
grid = [list(input()) for _ in range(N)]
# print(grid)
K = int(input())

#범위 내 있는지 확인하는 함수
def in_range(h,y):
    return 0<= h <N and 0<= y < N

#시작 지점 설정 함수, if 문과 else if 4개로 상,우,하,좌 중 어디인지 확인해야함.
def getStart(N,K):
    if K <= N :
        return 0, K-1, 2
    elif N < K and K <= N*2:
        return K-N-1, N-1, 3
    elif N*2 < K and K <= N*3:
        return  N-1, (N*3) - K, 0
    else:
        return (N*4)- K, 0 , 1

#방향 전환 함수
def getDirection(d, m):
    if m == '/':
        return (d + 1) % 4 if d % 2 == 0 else (d - 1 + 4) % 4
    else:  # mirror == '\'
        return (d - 1 + 4) % 4 if d % 2 == 0 else (d + 1) % 4


#방향 바꾸기 쉽게 저장
commands = {'U':0, 'R':1, 'D': 2, 'L':3}

#위치 방향표
dhs, dys = [-1,0,1,0],[0,1,0,-1]

#시작 지점 구하기
h, y, d = getStart(N, K)
# print(sh, sy, d)

#부딪힌 횟수
count = 0

#현재 command상 값이랑 방향표 값이랑 차이 살펴보기
#ex. D인데(2) /를 만나면 시계방향, \를 만나면 반시계 방향
#ex2. U인데(0) /를 만나면 시계 방향, \를 만나면 반시계 방향
#ex3. R인데(1) /를 만나면 반시계 방향, \를 만나면 시계 방향
#ex4. L인데(3) /를 만나면 반시계 방향, \를 만나면 시계 방향

while True:
    #방향 업데이트
    nh, ny = h+dhs[d], y+dys[d]

    if not in_range(nh, ny):
        break
        
    d = getDirection(d, grid[h][y])
    h, y = nh, ny
    count += 1  

        
    # #방향 업데이트
    # d = getDirection(d, grid[h][y])
    
print(count)