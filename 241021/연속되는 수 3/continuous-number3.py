N = int(input())
nums = [int(input()) for _ in range(N)]
maxNum = []
plus = 0
minus = 0

for i in range(len(nums)):
    if nums[i] > 0:
        maxNum.append(minus)
        minus = 0
        plus += 1
    else:
        maxNum.append(plus)
        plus = 0
        minus += 1
        
maxNum.append(plus)
maxNum.append(minus)

print(max(maxNum))