N = int(input())
nums = list(map(int, input().split()))
max_num = -1
for i in range(len(nums)):
    for j in range(i+2,len(nums)):
        max_num = nums[i]+nums[j] if nums[i]+nums[j] > max_num else max_num

print(max_num)
        
    