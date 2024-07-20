n, m = map(int, input().split());
numList = map(int, input().split());
count = 0

for i in numList:
    if i == m:
        count += 1;

print(count)