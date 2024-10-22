N, M, K = map(int, input().split())
students = {}
ans = 0
for i in range(1,M+1):
    students[i] = 0

for i in range(M):
    penalty = int(input())
    students[penalty] += 1
    if students[penalty] >= K:
        ans = penalty
        break

if ans:
    print(ans)
else:
    print(-1)