# from itertools import combinations
# import sys
# N, S = map(int, input().split())
# arr = list(map(int, input().split()))
# now = sys.maxsize
# # Write your code here!

# for cs in combinations(arr, N-2):
#     if abs(S - sum(cs)) < now :
#         now = S - sum(cs)

# print(now)
from itertools import combinations
import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))
now = sys.maxsize

# 모든 길이의 부분집합 고려
for r in range(N + 1):
    for cs in combinations(arr, r):
        diff = abs(S - sum(cs))
        if diff < now:
            now = diff

print(now)
