even_sum = 0
odd_sum = 0
count = 0

nums = list(map(int, input().split()))

for i in range(len(nums)):
    if i == 0:
        pass
                        
    if (i+1) % 2 == 0:
        even_sum += nums[i]

    if (i+1) % 3 == 0:
        odd_sum += nums[i]
        count += 1

print(f"{even_sum} {odd_sum/count:.1f}")