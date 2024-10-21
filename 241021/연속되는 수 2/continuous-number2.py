N = int(input())
nums = [int(input()) for _ in range(N)]
maxNum = []
cnt = 1
for i in range(1,len(nums)):
    if nums[i] != nums[i - 1]:
        maxNum.append(cnt)
        cnt = 1
    else:
        cnt += 1
maxNum.append(cnt)
print(max(maxNum))