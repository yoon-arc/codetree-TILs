n, t = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 1
getMax = []

for i in range(len(nums)-1):
    if nums[i] < nums[i+1] and nums[i]>3:
        cnt += 1
    else:
        getMax.append(cnt)
        cnt = 1

# print(getMax)
getMax.append(cnt)

if max(getMax) == 1:
    print(0)
else:
    print(max(getMax))