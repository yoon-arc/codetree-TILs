import sys
N = int(input())
loc = [tuple(map(int, input().split())) for _ in range(N)]

#시작, 끝, 중간 지점 기록
# start = loc[0]
# end = loc[-1]
# points = loc[1:N]

#최저 점수
short = sys.maxsize

#기준점이 되는
p = 0

#계산하기
for i in range(1, N-1):
    dist = 0
    now_I = 0
    for j in range(1,N):
        if j == i:#현재 기준점이 되는 숫자인 인덱스 i를 스킵
            continue
        dist += abs(loc[now_I][0]-loc[j][0])+abs(loc[now_I][1]-loc[j][1])
        now_I = j
    short = min(short, dist)

print(short)
    
