even_sum = 0
odd_sum = 0
count = 0

nums = list(map(int, input().split()))

for i in range(1, len(nums)):
    if i % 2 == 1:
        even_sum += nums[i]

    if i % 2 == 0:
        odd_sum += nums[i]
        count += 1

print(f"{even_sum} {odd_sum/count}")