# 두번 이상 지나간 영역의 크기 출력
# [2, L] -> 왼쪽으로 2만큼 이동
# [5, R] -> 오른쪽으로 5만큼 이동
# 2번 이상 지나간 구간을 모두 출력
# 앞선 인덱스의 

# 최소 모두 10씩 더해야함!! OFFSET

n = int(input())
counts = [0]*1000
moves = [input().split() for _ in range(n)]
location = 500

for i in moves:
    if i[1] == 'R':
        for j in range(location, location+int(i[0])):
            counts[j] += 1
        location += int(i[0])
        
    elif i[1] == 'L':
        for j in range(location-int(i[0]), location):
            counts[j] += 1
        location -= int(i[0])
        


total = 0
for i in range(len(counts)):
    if counts[i] >= 2:
        total += 1

print(total)