# N, T 입력 받기
N, T = map(int, input().split())
grid = []

# 명령들 입력 받기
commands = list(input())

# for문 N번만큼, input list
for _ in range(N):
    grid.append(list(map(int, input().split())))

#방향키
dhs,dys = [-1,0,1,0],[0,1,0,-1]

#시작 값 설정
s = (N-1)//2
h,y = s,s
d = 0

#범위 내인지 함수
def in_range(h,y):
    return 0<=h<N and 0<=y<N

#방향 설정 함수
def get_direction(c):
    return (d-1+4)%4 if c == 'L' else (d+1)%4
#총합
result = grid[h][y]


#for문(T안에서 돌기)
for c in commands:    
    if c != 'F' :
        d = get_direction(c)
        continue
        
    nh, ny = h+dhs[d],y+dys[d]
    if in_range(nh,ny):
        h, y = nh, ny
        result += grid[h][y]
        



    #범위 밖일 시 continue

   
    # result += grid[h][y]

    

print(result)