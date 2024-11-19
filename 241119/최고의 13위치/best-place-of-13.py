N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

max_count = 0
for i in range(N):
    for j in range(N-2):
        max_count = max(max_count, grid[i][j]+grid[i][j+1]+grid[i][j+2])

print(max_count)