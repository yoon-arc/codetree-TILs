#명령을 반복할 횟수
N = int(input())
#방향 전환용, E , S, W, N
dys, dhs = [1,0,-1,0],[0,1,0,-1]
dirc = {'E':0, 'S':1, 'W':2, 'N':3}

#처음 출발 지점 설정(0,0)
y = h = 0

#시간 누적
now_time = ans = 0

#반복문 - 횟수만큼 명령문 반복
for i in range(N):
    
    #명령문 입력
    d, s = input().split()
    s = int(s)
    
    #반복문 - 현재값 업데이트
    for j in range(s):
        now_time += 1
        y, h = y+dys[dirc[d]],h+dhs[dirc[d]]

        if y == 0 and h == 0:
            ans = now_time
            break

if ans:
    print(ans)
else:
    print(-1)

#0,0인지 확인
    #맞다면 답 변수에 시간 누적값 대입 후 break

#답 변수 체크하고 있으면 print 없으면 -1