n, t = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
getMax = []

for i in range(n):
    if nums[i]>t:
        cnt += 1
    else:
        getMax.append(cnt)
        cnt = 0

# print(getMax)
getMax.append(cnt)

if max(getMax) == 0:
    print(0)
else:
    print(max(getMax))