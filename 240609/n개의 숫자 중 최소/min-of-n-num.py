import sys
N = int(input())
M = list(map(int, input().split()))
min_val = sys.maxsize


for i in M:
    if i <= min_val:
        min_val = i


print(min_val, M.count(min_val))