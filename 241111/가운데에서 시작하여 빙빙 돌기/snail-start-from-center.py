#n 입력받기
n = int(input())

#입력할 체크판 만들기
check = [ [0]*n for _ in range(n)]
#중간값 미리 입력
s = (n-1)//2
check[s][s] = 1

#시작 지점 설정하기 -> 1입력
h, y = n-1, n-1
d = 0



#방향 조절판 설정
dhs, dys = [0,-1,0,1],[-1,0,1,0]

#범위인지 확인할 함수
def in_range(h,y):
    return 0<= h<n and 0<=y<n

#for문
for i in range(n*n,1,-1):
    nh, ny = h+dhs[d], y+dys[d]
    if not in_range(nh,ny) or check[h][y] != 0:
        d = (d+1)%4
    check[h][y] = i
    h, y = h+dhs[d], y+dys[d]

#출력
for line in check:
    print(*line, sep=" ")