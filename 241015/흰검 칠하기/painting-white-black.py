n = int(input())  # 명령의 개수
colors = [0] * 1000  # 색상 배열 초기화 ('0'은 아직 색이 결정되지 않음을 의미)
counts = [0] * 1000  # 카운트 배열 초기화
moves = [input().split() for _ in range(n)]  # 이동 명령 입력
now = 500  # 시작 위치 설정

for move in moves:
    steps = int(move[0])  # 이동할 칸 수
    direction = move[1]   # 이동 방향 ('L' 또는 'R')

    if direction == 'R':
        # 오른쪽으로 이동
        for j in range(now, now + steps):
            counts[j] += 1
            if counts[j] >= 4:
                colors[j] = 'G'  # 카운트가 4 이상이면 'G'로 고정
            elif colors[j] != 'G':  # 'G'가 아닌 경우에만 'B'로 덮음
                colors[j] = 'B'
        now += steps  # 현재 위치 업데이트

    elif direction == 'L':
        # 왼쪽으로 이동
        for j in range(now - steps, now):
            counts[j] += 1
            if counts[j] >= 4:
                colors[j] = 'G'  # 카운트가 4 이상이면 'G'로 고정
            elif colors[j] != 'G':  # 'G'가 아닌 경우에만 'W'로 덮음
                colors[j] = 'W'
        now -= steps  # 현재 위치 업데이트

# 'W', 'B', 'G'의 개수 출력
print(colors.count('W'), colors.count('B'), colors.count('G'))