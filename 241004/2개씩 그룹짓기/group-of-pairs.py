N = int(input())
nList = list(map(int, input().split()))

# 숫자 리스트를 오름차순으로 정렬합니다.
nList.sort()

# 최소화된 최대 그룹의 합을 구합니다.
max_sum = 0
for i in range(N):
    # 가장 작은 값과 가장 큰 값을 그룹으로 묶습니다.
    pair_sum = nList[i] + nList[2 * N - 1 - i]
    # 각 그룹의 합 중 최댓값을 기록합니다.
    max_sum = max(max_sum, pair_sum)

print(max_sum)