n, k = map(int, input().split())
nums = list(map(int, input().split()))

max_num = 0
for i in range(n-k+1):
    if sum(nums[i:i+k]) > max_num:
        max_num = sum(nums[i:i+k])
print(max_num)