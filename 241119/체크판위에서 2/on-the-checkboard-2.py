# R*C 크기의 직사각형, 칸은 W,B로 이뤄져 있음
# 0,0에서 R,C로 이동하는 경우의 수
# 1. 현재 색과 이동할 곳의 색이 달라야함
# 2. 이동할 때 적어도 행과 열이 한칸보다 많이
# 3. 시작, 도착을 제외하고 도달한 곳이 두곳이어야함.

# 경우의 수니까 지금이랑 다른 갯수만큼 카운트하고
# 서로 곱해야할듯(실시간으로 곱하기)

#R눈 세로(행), C는 가로(열)
h, y = map(int, input().split())
grid = [list(input().split()) for _ in range(h)]

count = 0
# def check()

for i in range(1, h):
    for j in range(1, y):
        for k in range(i + 1, h - 1):
            for l in range(j + 1, y - 1):
                # 그 중 색깔이 전부 달라지는 경우에만 개수를 세줍니다.
                #행의 수가 항상 5 미만으로 고정되어 있기 때문에 실행 가능한 것..
                if grid[0][0] != grid[i][j] and \
                   grid[i][j] != grid[k][l] and \
                   grid[k][l] != grid[h - 1][y - 1]:
                    count += 1
print(count)