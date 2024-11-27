import sys
N = int(input())
# 방 번호, 방 안의 사람
rooms = [(i, int(input())) for i in range(1,N+1)]
# print(rooms)

# for x,y in rooms:
#     print(x,y)
min_num = sys.maxsize
# 출발 지점
for s in range(1,N+1):
    # 1번 방부터 N번째 방까지 반복
    sums = 0
    for r,p in rooms:
        # r = 방 번호 , p = 방 안의 사람
        #출발 지점과 현재 방 사이의 거리 구하기
        if s<=r:
            repeat = r-s
        elif s>r:
            repeat = N-(s-r)
        sums += (p*repeat)
    # print(sums)
    if sums < min_num : 
        min_num = sums

print(min_num)