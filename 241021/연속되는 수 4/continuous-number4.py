N = int(input())
nums = [int(input()) for _ in range(N)]
maxNum = []
cnt = 1

for i in range(len(nums)-1):
    if nums[i] < nums[i + 1]:
        maxNum.append(cnt)
        cnt += 1
    else:
        maxNum.append(cnt)
        cnt = 1
#     print(maxNum)
    
maxNum.append(cnt)

print(max(maxNum))