import sys
min_case = sys.maxsize
n = int(input())
houses = list(map(int, input().split()))

for i in range(n):
    moves = 0
    for p in range(n):
        moves += (houses[p]*abs(i-p))
    if moves < min_case:
        min_case = moves
print(min_case)