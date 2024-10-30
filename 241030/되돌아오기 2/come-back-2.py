N = list(input())

#방향 전환용 N,E,S,W
dys, dhs = [-1,0,1,0],[0,1,0,-1]

#시작 좌표
y = h = 0

#현재 방향
d = 0

#총 시간 카운트용 변수
time = ans = 0

#명령 반복문
for c in N:
    #L일 때, 방향 바꾸기, 시간 증가 시키기, continue하기
    if c == 'L':
        time += 1
        d = (d-1+4)%4
        continue
        
    #R일 때, 방향 바꾸기, 시간 증가 시키기, continue하기
    elif c == 'R':
        time += 1
        d = (d+1)%4
        continue
    #나머지, 시간 증가 시키고 현재 d에 따라 더하기
    time += 1
    y,h = y+dys[d], h+dhs[d]

    #시작점인지 아닌지 확인하기, 맞다면 ans에 현재값 대입
    if y == 0 and h == 0:
        ans = time
        break
        


#ans에 값 있는지 없는지에 따라 -1출력
if ans:
    print(ans)
else:
    print(-1)