nums = list(map(int, input().split()))
sumUp = 0
count = 0

for i in nums:
    if i >= 250:
        break

    else:
        sumUp += i
        count += 1


print(f"{sumUp} {(sumUp/count):.1f}")